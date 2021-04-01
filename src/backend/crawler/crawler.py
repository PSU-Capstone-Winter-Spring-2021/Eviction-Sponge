import functools

import requests
from requests import Session
from dataclasses import replace
from src.backend.crawler.util import URL, Payload, LRUCache
from src.backend.crawler.parsers.node_parser import NodeParser
from src.backend.crawler.parsers.param_parser import ParamParser
from src.backend.crawler.parsers.record_parser import RecordParser
from src.backend.crawler.parsers.case_parser import CaseParser
from src.backend.models.case_model import CaseCreator, EditStatus
from concurrent.futures.thread import ThreadPoolExecutor


class UnableToReachOECI(Exception):
    pass


class InvalidLoginCreds(Exception):
    pass


class Crawler:
    cached_links = LRUCache(1000)

    # attempt login function that takes in a username and password and
    # returns a success (0) or throws an exception detailing why failure occurred
    # attempts to login to the OECI website
    @staticmethod
    def attempt_login(username, password):
        url = URL.login_url()
        payload = {'UserName': username, 'Password': password, 'ValidateUser': '1',
                   'dbKeyAuth': 'JusticePA', 'SignOn': 'Sign+On'}
        r = requests.post(url, payload)
        content = r.text
        if "Case Records" in content:
            # success
            return content
        elif "Oregon eCourt is temporarily unavailable due to maintenance" in content:
            raise UnableToReachOECI
        else:
            raise InvalidLoginCreds

    @staticmethod
    def search(session: Session, login_response, first_name, last_name, middle_name=""):
        # What is login_response? used to verify that the credentials are still valid.
        # boolean function that attempts to login again

        # get search page, post it with node data
        search_url = URL.search_url()
        node_response = Crawler._fetch_search_page(session, search_url, login_response)

        # generate a list of case records, specifically a list of CaseSummary from case_parser.py
        # (for each case: case #, style, filed/location, type/status, and link to detailed case info)
        search_result = Crawler._search_record(session, node_response, search_url, first_name, last_name, middle_name)

        if len(search_result.cases) >= 300:  # max number of cases we want to address
            raise ValueError(
                f"Found {len(search_result.cases)} matching cases, exceeding the limit of 300."
            )

        # read the records and generate a list of relevant cases
        with ThreadPoolExecutor(max_workers=50) as executor:
            oeci_cases = {}
            for oeci_case in executor.map(functools.partial(Crawler._read_case, session=session), search_result):
                key = oeci_case.case_number
                value = (oeci_case.style, oeci_case.location, oeci_case.violation_type, oeci_case.current_status,
                         oeci_case.date, "judgement not implemented yet")
                oeci_cases.update({key: value})
        return oeci_cases

    @staticmethod
    def _fetch_search_page(session, search_url, login_response):
        # get the node_id of the parser given the login_response, and post it
        node_parser = NodeParser()
        node_parser.feed(login_response)
        payload = {"NodeID": node_parser.node_id, "NodeDesc": "All+Locations"}
        return session.post(search_url, data=payload, timeout=30)

    @staticmethod
    def _search_record(session, node_response, search_url, first_name, last_name, middle_name):
        param_parser = ParamParser()
        param_parser.feed(node_response.text)
        payload = Payload.payload(param_parser, last_name, first_name, middle_name)
        response = session.post(search_url, data=payload, timeout=30)

        record_parser = RecordParser()
        record_parser.feed(response.text)
        return record_parser.cases

    @staticmethod
    def _read_case(session, case):
        # cache the link
        if session:
            session_response = session.get(case.case_detail_link)
            Crawler.cached_links[case.case_detail_link] = session_response
        else:
            session_response = Crawler.cached_links[case.case_detail_link]

        # check if response has acceptable code and text exists
        if session_response.status_code != 200 or session_response.text is None:
            raise ValueError(f"Failed to fetch case detail page. Please rerun the search.")

        case_parser_data = CaseParser.feed(session_response.text)
        # balance_due_in_cents = CaseCreator.compute_balance_due_in_cents(case_parser_data.balance_due)
        closed_date = case_parser_data.closed_date

        updated_summary = replace(case, date=closed_date, edit_status=EditStatus.UNCHANGED)
        return updated_summary
