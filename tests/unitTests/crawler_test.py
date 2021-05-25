import os
import sys

import pytest

from src.backend.crawler.crawler import UnableToReachOECI, InvalidLoginCreds, Crawler
from tests.class_mocks import MockRequest, MockSession, MockURL

# Need this little tidbit for pytest to work
from src.backend.crawler.util import URL

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.backend.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


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
