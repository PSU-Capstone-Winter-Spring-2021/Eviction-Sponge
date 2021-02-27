import os
import sys

import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.backend.endpoints import oeci_login
from src.backend.endpoints.oeci_login import OeciLogin

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


def test_login_success(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Successful login response"))
    response = login(client, 'username', 'password')
    assert response.status_code == 201


def test_login_missing_username_fail(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Failed login respose"))
    response = login(client, None, 'password')
    assert response.status_code == 400


def test_login_missing_password_fail(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Failed login respose"))
    response = login(client, 'password', None)
    assert response.status_code == 400


def test_login_missing_username_and_password_fail(client, monkeypatch):
    # create mock for Crawler
    monkeypatch.setattr(oeci_login.Crawler, "attempt_login", mock_login("Failed login respose"))
    response = login(client, None, None)
    assert response.status_code == 400