import os
import re
import sys

import pytest
import requests
from src.backend.crawler.crawler import Crawler
from src.backend.endpoints import search
from src.backend.endpoints.search import Search

# Need this little tidbit for pytest to work
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.backend.app import create_app


@pytest.fixture
def client():
    app = create_app('development')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Have to actually post data to /search to call Search's post function
def post_data(client, first_name, last_name, middle_name):
    return client.post('/search', json={
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name
    }, follow_redirects=True)


# Call Search's post function, but pass no data
def post_no_data(client):
    return client.post('/search', follow_redirects=True)


def mock_search_error(code, message):
    raise Exception(str(code) + ' ' + message)


def mock_crawler_attempt_login(session, username, password):
    return lambda username, password: ''


def mock_crawler_search(session, login_creds, first_name, last_name, middle_name):
    return [{'12345': {'style': 'style', 'location': 'location', 'violation_type': 'type',
                       'status': 'status', 'date': '09/09/9999', 'judgements': ['judgement1', 'judgement2'],
                       'eligibility': (True, 'Eligible')}}]


def mock_requests_Session():
    return None


def mock_oeci_login_params(request):
    return "username", "password"


def test_none_data_returns_error(client, monkeypatch):
    # The error results in an abort.  Patching with a generic exception to test for the code + message
    monkeypatch.setattr(search, "error", mock_search_error)
    with pytest.raises(Exception) as excep:
        post_no_data(client)
    assert excep.match(r"400")
    assert excep.match(r"Missing first and last name")


def test_missing_first_name_returns_error(client, monkeypatch):
    # The error results in an abort.  Patching with a generic exception to test for the code + message
    monkeypatch.setattr(search, "error", mock_search_error)
    with pytest.raises(Exception) as excep:
        post_data(client, '', 'last_name', 'middle_name')
    assert excep.match(r"400")
    assert excep.match(r"Missing first name")


def test_missing_last_name_returns_error(client, monkeypatch):
    # The error results in an abort.  Patching with a generic exception to test for the code + message
    monkeypatch.setattr(search, "error", mock_search_error)
    with pytest.raises(Exception) as excep:
        post_data(client, 'first_name', '', 'middle_name')
    assert excep.match(r"400")
    assert excep.match(r"Missing last name")


def test_missing_middle_name_works_fine(client, monkeypatch):
    monkeypatch.setattr(Search, "_oeci_login_params", mock_oeci_login_params)
    monkeypatch.setattr(Crawler, "attempt_login", mock_crawler_attempt_login)
    monkeypatch.setattr(Crawler, "search", mock_crawler_search)
    monkeypatch.setattr(requests, "Session", mock_requests_Session)

    response = post_data(client, 'first_name', 'last_name', '')

    # Grab the first key, check if it matches what mock_search returned
    contents = response.data.decode("utf-8")
    contents = re.search(r"\[{\"[0-9]*", contents).group()
    assert response.status_code == 200
    assert re.sub("\[{\"", '', contents) == str(12345)


def test_full_search_success(client, monkeypatch):
    monkeypatch.setattr(Search, "_oeci_login_params", mock_oeci_login_params)
    monkeypatch.setattr(Crawler, "attempt_login", mock_crawler_attempt_login)
    monkeypatch.setattr(Crawler, "search", mock_crawler_search)
    monkeypatch.setattr(requests, "Session", mock_requests_Session)

    response = post_data(client, "first_name", "last_name", "middle_name")

    # Grab the first key, check if it matches what mock_search returned
    contents = response.data.decode("utf-8")
    contents = re.search(r"\[{\"[0-9]*", contents).group()
    assert response.status_code == 200
    assert re.sub("\[{\"", '', contents) == str(12345)
