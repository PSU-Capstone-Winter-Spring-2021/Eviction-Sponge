from dataclasses import replace
from crawler.util import URL, Payload, LRUCache
from crawler.parsers.node_parser import NodeParser
from crawler.parsers.param_parser import ParamParser
from crawler.parsers.record_parser import RecordParser
from crawler.parsers.case_parser import CaseParser
import eligibility_eval


class UnableToReachOECI(Exception):
    pass


class InvalidLoginCreds(Exception):
    pass


class Crawler:
    cached_links = LRUCache(1000)

    # Attempt to login to the OECI database.  Throws a relevant exception when unable to reach it
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

    # Search the OECI database for eviction cases relevant to the search name
    # Return a j-son style dictionary (for easy json.dump'ing in search.py) of cases in the form:
    # {case_number: style, location, type, status, closed date, list of judgements, eligibility}
    # (Types: {int : str, str, str, str, datetime, list[str], (bool, str) tuple})
    @staticmethod
    def search(session, login_response, first_name, last_name, middle_name=""):
        # login_response is used to verify that the credentials are still valid,
        # it is the return value of Crawler.attempt_login()

        search_url = URL.search_url()
        node_response = Crawler._fetch_search_page(session, search_url, login_response)

        # generate a list of case records (see CaseSummary in case_model.py)
        # the OECI database named the column 'style', it's the name of the case (i.e. "John Hancock V. John Smith")
        search_result = Crawler._search_record(session, node_response, search_url, first_name, last_name, middle_name)

        # eviction cases will be of the following types
        ACCEPTABLE_TYPES = ["Forcible Entry Detainer: Residential",
                            "Landlord/Tenant - Residential or Return of Personal Property"]

        eviction_cases = []
        for case in search_result:
            # Skip over non-eviction cases
            if case.violation_type not in ACCEPTABLE_TYPES:
                continue
            eviction_case = Crawler._read_case(session, case)

            # Test if this eviction is eligible for expungement:
            # Aside: eligibility_eval.is_eligible is non-intuitive, but makes testing so much easier than
            # from ... import is_eligible and calling is_eligible(...)
            eligibility = eligibility_eval.is_eligible(eviction_case.current_status, eviction_case.closed_date, eviction_case.judgements)

            # Grab the OECI ID number for this case, to be used when calling the case detail endpoint
            case_id = case.case_detail_link.split('CaseID=')[1]

            # Build a dictionary of all eviction cases found.  Using json format
            # Note: converting date to a string manually in the form mm/dd/yyyy, as otherwise the default date->string
            #       is called and includes the time
            key = eviction_case.case_number
            value = {'style': eviction_case.style,
                     'case_id': case_id,
                     'location': eviction_case.location,
                     'violation_type': eviction_case.violation_type,
                     'status': eviction_case.current_status,
                     'complaint_date': eviction_case.complaint_date,
                     'closed_date': eviction_case.closed_date.strftime("%m/%d/%Y"),
                     'judgements': eviction_case.judgements,
                     'eligibility': eligibility,
                     'balance': eviction_case.balance_due}
            eviction_cases.append({key: value})
            # Types {int : str, str, str, str, str, list[str], (bool, str) tuple}
        return eviction_cases

    # Grab the node_id of the parser given the login_response, and post it
    @staticmethod
    def _fetch_search_page(session, search_url, login_response):
        node_parser = NodeParser()
        node_parser.feed(login_response)
        payload = {"NodeID": node_parser.node_id, "NodeDesc": "All+Locations"}

        return session.post(search_url, data=payload, timeout=30)

    # Search the database for cases that match the names provided and return the summaries of each
    # (specifically, the info provided on OECI's search page: case #, style, date/location, type/status,
    # and case_detail_link)
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
        # cache the link for future use
        if session:
            # Dear Future Maintainer,
            #       If you're trying to make this crawler go faster, session.get is your issue.
            session_response = session.get(case.case_detail_link)
            Crawler.cached_links[case.case_detail_link] = session_response
        else:
            session_response = Crawler.cached_links[case.case_detail_link]

        # check if response has acceptable code and text exists
        if session_response.status_code != 200 or session_response.text is None:
            raise ValueError(f"Failed to fetch case detail page. Please rerun the search.")

        # parse the case to gather the actual closed date and judgement list, then replace the default with them
        case_parser_data = CaseParser.feed(session_response.text)

        balance_due = case_parser_data.money
        closed_date = case_parser_data.closed_date
        complaint_date = case_parser_data.complaint_date
        judgements = case_parser_data.judgements
        updated_summary = replace(case, complaint_date=complaint_date, closed_date=closed_date, judgements=judgements, balance_due=balance_due)


        return updated_summary

    @staticmethod
    def fetch_case_detail_link(url):
        return Crawler.cached_links[url]
