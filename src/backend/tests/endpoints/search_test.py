from typing import List, Any, Callable
import pytest

from src.backend.crawler.crawler import Crawler
from src.backend.tests.endpoints.endpoint_util import EndpointShared
from src.backend.models.case_model import OeciCase

@pytest.fixture
def service():
    return EndpointShared()

def mock_login(return_value):
    return lambda s, username, password, close_session=False: return_value

def mock_search(service, mocked_record_name) -> Callable[[Any, Any, Any, Any, Any, Any], List[OeciCase]]:
    def compute_cases(s, login_response, first_name, last_name, middle_name):
        record = service.mock_record[mocked_record_name]
        return record.cases
    return compute_cases

def test_search(service, monkeypatch):
    monkeypatch.setattr(Crawler, "attempt_login", mock_login("Successful login response"))
    monkeypatch.setattr(Crawler, "search", mock_search(service, "john_smith"))
    service.client.post("/login", json={"oeci_username": "correctusername", "oeci_password": "correctpassword"}
    )
    assert service.client.cookie_jar._cookies["localhost.local"]["/"]["oeci_token"]

    response = service.client.post("/search", json=service.search_resquest_data)
    assert response.status_code == 200








