import functools

import requests
from requests import Session
from dataclasses import replace
from crawler.util import URL, Payload, LRUCache
from crawler.parsers.node_parser import NodeParser
from crawler.parsers.param_parser import ParamParser
from crawler.parsers.record_parser import RecordParser
from crawler.parsers.case_parser import CaseParser
from models.case_model import CaseCreator, EditStatus
from concurrent.futures.thread import ThreadPoolExecutor
from eligibility_eval import isEligible


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
    def attempt_login(session, username, password):
        url = URL.login_url()
        payload = {'UserName': username, 'Password': password, 'ValidateUser': '1',
                   'dbKeyAuth': 'JusticePA', 'SignOn': 'Sign+On'}
        r = session.post(url, payload)
        content = r.text
        if "Case Records" in content:
            # success
            return content
        elif "Oregon eCourt is temporarily unavailable due to maintenance" in content:
            raise UnableToReachOECI
        else:
            raise InvalidLoginCreds

    @staticmethod
    def search(session, login_response, first_name, last_name, middle_name=""):
        # login_response is used to verify that the credentials are still valid

        # We don't appear to need the following, but just in case it breaks again:
        # url = URL.login_url()
        # payload = {'UserName': '', 'Password': '', 'ValidateUser': '1',
        #            'dbKeyAuth': 'JusticePA', 'SignOn': 'Sign+On'}
        # r = requests.post(url, payload)

        search_url = URL.search_url()
        node_response = Crawler._fetch_search_page(session, search_url, login_response)

        # generate a list of case records, specifically a list of CaseSummary from case_parser.py
        # (for each case: case #, style, filed/location, type/status, and link to detailed case info)
        search_result = Crawler._search_record(session, node_response, search_url, first_name, last_name, middle_name)

        if len(search_result) >= 300:  # max number of cases we want to address
            raise ValueError(
                f"Found {len(search_result)} matching cases, exceeding the limit of 300."
            )

        # read the records and generate a list of relevant cases
        ACCEPTABLE_TYPES = ["Forcible Entry Detainer: Residential",
                            "Landlord/Tenant - Residential or Return of Personal Property"]
        with ThreadPoolExecutor(max_workers=50) as executor: # TODO: remove this, it don't do much
            oeci_cases = {}
            # below line is a fancy way of replacing the default date and judgement list with the actual closed date
            # and judgement list found when parsing the case

            # for oeci_case in executor.map(functools.partial(Crawler._read_case, session=session), search_result):
            cases = []
            for result in search_result:
                cases.append(Crawler._read_case(session, result))
            for oeci_case in cases:
                # Skip over non-eviction cases
                if oeci_case.violation_type not in ACCEPTABLE_TYPES:
                    continue

                # Test if this eviction is eligible for expungement:
                eligibility = isEligible(oeci_case.current_status, oeci_case.date, oeci_case.judgements)  # (Bool, Str)

                # Build a dictionary of all eviction cases found.  Using json format
                key = oeci_case.case_number
                value = {'style': oeci_case.style, 'location': oeci_case.location,
                         'violation_type': oeci_case.violation_type, 'status': oeci_case.current_status,
                         'date': oeci_case.date, 'judgements': oeci_case.judgements, 'eligibility': eligibility}
                oeci_cases.update({key: value})
                # Types {int : str, str, str, str, datetime, list[str], (bool, str) tuple}
        return oeci_cases

    # Grab the node_id of the parser given the login_response, and post it
    @staticmethod
    def _fetch_search_page(session, search_url, login_response):
        node_parser = NodeParser()
        node_parser.feed(login_response)
        payload = {"NodeID": node_parser.node_id, "NodeDesc": "All+Locations"}
        return session.post(search_url, data=payload, timeout=30)

    # Search the database for cases that match the names provided, and feed the results to RecordParser
    # for later parsing
    @staticmethod
    def _search_record(session, node_response, search_url, first_name, last_name, middle_name):
        param_parser = ParamParser()
        param_parser.feed(node_response.text)
        payload = Payload.payload(param_parser, last_name, first_name, middle_name)
        response = session.post(search_url, data=payload, timeout=30)

        record_parser = RecordParser()
        record_parser.feed(response.text)
        return record_parser.cases

    # Parse the detailed case page for judgements and the closed date of a case
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

        # parse the case to gather the actual closed date and judgement list, then replace the default with them
        case_parser_data = CaseParser.feed(session_response.text)
        # balance_due_in_cents = CaseCreator.compute_balance_due_in_cents(case_parser_data.balance_due)
        closed_date = case_parser_data.closed_date
        judgements = case_parser_data.judgements

        updated_summary = replace(case, date=closed_date, judgements=judgements, edit_status=EditStatus.UNCHANGED)
        return updated_summary
