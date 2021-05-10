import os
import sys

import pytest
import requests
from datetime import datetime
from flask import json, request
from src.backend.crawler.crawler import Crawler


# Need this little tidbit for pytest to work
from src.backend.endpoints.search import Search

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.backend.app import create_app


@pytest.fixture
def client():
    app = create_app('development')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# weird name to avoid namespace cluttering issues, ideally it'd just be called search.  It triggers search.py's post()
def search(client, first_name, last_name, middle_name):
    return client.post('/search', data={
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name'
    }, follow_redirects=True)


def search_none_data(client):
    return client.post('/search', data={
    }, follow_redirects=True)


def mock_login(session, username, password):
    return lambda username, password: "logged in"


def mock_search(session, login_creds, first_name, last_name, middle_name):
    return [{'12345': {'style': 'style', 'location': 'location', 'violation_type': 'type',
                       'status': 'status', 'date': '09/09/9999', 'judgements': ['judgement1', 'judgement2'],
                       'eligibility': (True, 'Eligible')}}]


def mock_Session():
    return None


def mock_oeci_login_params(request):
    return "username", "password"


def test_none_data(client):
    response = search_none_data(client)
    assert response.status_code == 400


# NOTE: TEST NOT FUNCTIONAL YET. WILL ALWAYS FAIL
def test_full_search(client, monkeypatch):
    monkeypatch.setattr(Search, "_oeci_login_params", mock_oeci_login_params)
    monkeypatch.setattr(Crawler, "attempt_login", mock_login)
    monkeypatch.setattr(Crawler, "search", mock_search)
    monkeypatch.setattr(requests, "Session", mock_Session)

    # search returns a json.dumps object. Turn it back into a dictionary w/ .json
    first_case_num = list((search(client, "first_name", "last_name", "middle_name")).json)[0]

    # the idea is to check that the first key of the dictionary returned is the '12345' we set it to, but
    # currently 'if data is None:' is being triggered and we're getting {message: Missing one for more required fields}
    assert first_case_num == '12345'

