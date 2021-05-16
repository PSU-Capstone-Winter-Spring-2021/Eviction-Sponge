import os
import sys
from datetime import datetime

import pytest

from src.backend import eligibility_eval
from src.backend.crawler.crawler import UnableToReachOECI, InvalidLoginCreds, Crawler
from tests.class_mocks import MockRequest, MockSession, MockURL, MockCaseSummary
from src.backend.crawler.util import URL
from src.backend.app import create_app

# Need this little tidbit for pytest to work
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


""" MOCKS """


def mock_is_eligible(current_status, closed_date, judgements):
    return True, "Eligible"


def mock_fetch_search_page(session, search_url, login_response):
    return "it doesn't really matter"


# Used specifically in test_search_returns_eviction_type_cases, returns a mix of eviction and non-eviction type cases
def mock_search_record_two_evictions_four_cases(session, node_response, search_url, first, last, middle):
    return [MockCaseSummary('100', 'style', 'location', datetime(9999, 9, 9), 'type', 'status', ['judgement'],
                            'detail link'),
            MockCaseSummary('101', 'style', 'location', datetime(9999, 9, 9), 'Forcible Entry Detainer: Residential',
                            'status', ['judgement'], 'detail link'),
            MockCaseSummary('102', 'style', 'location', datetime(9999, 9, 9), 'type', 'status', ['judgement'],
                            'detail link'),
            MockCaseSummary('103', 'style', 'location', datetime(9999, 9, 9),
                            'Landlord/Tenant - Residential or Return of Personal Property', 'status', ['judgement'],
                            'detail link')]


# Return a list of 301 elements.  Doesn't matter what the list consists of, since search() just tests length
def mock_search_record_three_hundred_and_one_cases(session, node_response, search_url, first, last, middle):
    cases = []
    for i in range(301):
        cases.append(str(i))
    return cases


def mock_read_case(session, case):
    return case


""" ATTEMPT_LOGIN TESTS """


# Test success path through attempt_login
def test_attempt_login_success(monkeypatch):
    # Replace the URL used with a fake one
    monkeypatch.setattr(URL, "login_url", MockURL().login_url)
    # Build a mock session that can be interacted with
    session = MockSession()
    mock_request = MockRequest()
    mock_request.set_text("Case Records")
    session.set_post_return(mock_request)

    result = Crawler.attempt_login(session, "", "")
    assert result == "Case Records"


# Test attempt_login failure due to database offline
def test_attempt_login_oeci_unavailable_throws_exception(monkeypatch):
    # Replace the URL used with a fake one
    monkeypatch.setattr(URL, "login_url", MockURL().login_url)
    # Build a mock session that can be interacted with
    session = MockSession()
    mock_request = MockRequest()
    mock_request.set_text("Oregon eCourt is temporarily unavailable due to maintenance")
    session.set_post_return(mock_request)

    with pytest.raises(UnableToReachOECI):
        Crawler.attempt_login(session, "", "")


# Test attempt_login failure due to invalid login credentials
def test_attempt_login_invalid_login_creds_throws_exception(monkeypatch):
    # Replace the URL used with a fake one
    monkeypatch.setattr(URL, "login_url", MockURL().login_url)
    # Build a mock session that can be interacted with
    session = MockSession()
    mock_request = MockRequest()
    mock_request.set_text("Any string that isn't from the above two tests")
    session.set_post_return(mock_request)

    with pytest.raises(InvalidLoginCreds):
        Crawler.attempt_login(session, "", "")


""" SEARCH TESTS """


# Give search four cases (two evictions, two non-evictions) and check that only the eviction cases are returned
def test_search_returns_eviction_type_cases(monkeypatch):
    # Need to mock URL, _fetch_search_page, _search_record, _read_case, and is_eligible. Oh boy.
    monkeypatch.setattr(URL, "search_url", MockURL().search_url)
    monkeypatch.setattr(Crawler, "_fetch_search_page", mock_fetch_search_page)
    monkeypatch.setattr(Crawler, "_search_record", mock_search_record_two_evictions_four_cases)
    monkeypatch.setattr(Crawler, "_read_case", mock_read_case)
    # Note that crawler uses eligibility_eval.is_eligible(...), not just is_eligible(...), so this works to patch it:
    # (if crawler called is_eligible(...) directly, this wouldn't patch the right is_eligible)
    # This is also why we can patch search_url
    monkeypatch.setattr(eligibility_eval, 'is_eligible', mock_is_eligible)

    cases = Crawler().search('', '', '', '', '')
    # Check that only two cases are returned, and that they are specifically case numbers 101 and 103
    # (see mock_search_record_two_evictions_four_cases)
    assert len(cases) == 2
    # python 3.3 made keys() return a dict_keys([]) instead of list[]
    assert '101' == list(cases[0].keys())[0]
    assert '103' == list(cases[1].keys())[0]


def test_search_over_three_hundred_cases_raises_value_error(monkeypatch):
    monkeypatch.setattr(URL, "search_url", MockURL().search_url)
    monkeypatch.setattr(Crawler, "_fetch_search_page", mock_fetch_search_page)
    monkeypatch.setattr(Crawler, "_search_record", mock_search_record_three_hundred_and_one_cases)

    with pytest.raises(ValueError):
        Crawler().search('', '', '', '', '')
