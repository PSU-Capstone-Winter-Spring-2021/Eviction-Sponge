""" NO LONGER USEFUL, NEEDS UPDATE.  KEEPING FOR REFERENCE
import os
import sys

import pytest

from src.backend.endpoints import oeci_login
from src.backend.crawler.crawler import UnableToReachOECI, InvalidLoginCreds

# Need this little tidbit for pytest to work
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.backend.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def login(client, username, password):
    return client.post('/login', data={
        "oecilogin": username,
        "oecipassword": password
    }, follow_redirects=True)


def mock_login(value):
    return lambda username, password: value


# TEST: (ideal situation) username/password accepted and login successful, result is status code 201
def test_login_success(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Successful login response"))
    response = login(client, 'username', 'password')
    assert response.status_code == 201


# TEST: failure due to missing username, result is status code 400 (missing data)
def test_login_missing_username_fail(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Failed login respose"))
    response = login(client, None, 'password')
    assert response.status_code == 400


# TEST: failure due to missing password, result is status code 400 (missing data)
def test_login_missing_password_fail(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Failed login respose"))
    response = login(client, 'password', None)
    assert response.status_code == 400


# TEST: failure due to missing username and password, result is status code 400 (missing data)
def test_login_missing_username_and_password_fail(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Failed login respose"))
    response = login(client, None, None)
    assert response.status_code == 400


# TEST: failure due to OECI database being unreachable
def throw_unable_to_reach_oeci(_, __):
    raise UnableToReachOECI()

def test_login_cant_reach_oeci_exception(client, monkeypatch):
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", throw_unable_to_reach_oeci)
    response = login(client, 'username', 'password')
    assert response.status_code == 404


# TEST: failure due to bad credentials
def throw_invalid_login_creds(_, __):
    raise InvalidLoginCreds()

def test_login_invalid_login_creds_exception(client, monkeypatch):
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", throw_invalid_login_creds)
    response = login(client, 'username', 'password')
    assert response.status_code == 401
"""
