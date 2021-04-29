import os
import sys

import pytest
from datetime import datetime
from flask import request
import requests
from src.backend.endpoints import search

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


def search(client, first_name, last_name, middle_name):
    return client.post('/search', data={
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name
    }, follow_redirects=True)


def search_none_data(client):
    return client.post('/search', data={
    }, follow_redirects=True)


def mock_login(session, username, password):
    return lambda username, password: "logged in"


def mock_search(session, login_creds, first_name, last_name, middle_name):
    return {12345: {"style", "location", "type", "status", datetime(9999, 9, 9), {"judgement1, judgement2"},
                    [True, "Eligible"]}}


def mock_oeci_login_params(request):
    return "username", "password"


def test_none_data(client):
    response = search_none_data(client)
    assert response.status_code == 400


def test_full_search(client, monkeypatch):
    # mock Crawler's attempt_login and search functions
    monkeypatch.setattr(search.Search, "_oeci_login_params", mock_oeci_login_params(request))
    monkeypatch.setattr(search.Crawler, "attempt_login", mock_login("username", "password"))
    monkeypatch.setattr(search.Crawler, "search", mock_search(request.session, "logged in", "first_name", "last_name", "middle_name"))

    response = search(client, "first_name", "last_name", "middle_name")
    assert response == {12345: {"style", "location", "type", "status", datetime(9999, 9, 9), {"judgement1, judgement2"},
                    [True, "Eligible"]}}
