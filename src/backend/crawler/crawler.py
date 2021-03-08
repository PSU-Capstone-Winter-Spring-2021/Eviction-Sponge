import functools

import requests
from requests import Session
from src.backend.crawler.util import URL, Payload, LRUCache
from src.backend.crawler.parsers.node_parser import NodeParser
from src.backend.crawler.parsers.param_parser import ParamParser
from concurrent.futures.thread import ThreadPoolExecutor


class UnableToReachOECI(Exception):
    pass


class InvalidLoginCreds(Exception):
    pass


# attempt login function that takes in a username and password and
# returns a success (0) or throws an exception detailing why failure occured
# attempts to login to the OECI website

class Crawler:
    cached_links = LRUCache(1000)

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
        # TODO: What is login_response?

        # get search page, post it with node data
        search_url = URL.search_url()
        node_response = Crawler._fetch_search_page(session, search_url, login_response)

        # get the record info out of node_response
        search_result = Crawler._search_record(session, node_response, search_url, first_name, last_name, middle_name)

        # read the records and generate a list of relevant cases
        with ThreadPoolExecutor(max_workers=50) as executor:
            oeci_cases = []
            for oeci_case in executor.map(functools.partial(Crawler._read_case, session=session), search_result.cases):
                oeci_cases.append(oeci_case)
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

        # TODO: write something to parse records retrieved, like their RecordParser

    @staticmethod
    def _read_case(session, case):
        # cache the link
        if session:
            cache_response = session.get(case.case_detail_link)
            Crawler.cached_links[case.case_detail_link] = cache_response
        else:
            cache_response = Crawler.cached_links[case.case_detail_link]

        if cache_response.status_code != 200 or not cache_response.text:
            raise ValueError(f"Failed to fetch case detail page. Please rerun the search.")

        # TODO: write something to parse the cache_response.txt into case_parser_data
        case_parser_data = CaseParser.feed(cache_response.text)

        # TODO: Here we'd select certain useful data items, find the balance due, etc for the case, and return that