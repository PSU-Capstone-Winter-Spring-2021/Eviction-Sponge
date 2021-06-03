import pytest
from tests.unitTests.endpointTests.endpoint_util import EndpointShared

@pytest.fixture
def service():
    return EndpointShared()

#Nothing else to test for partners page in the backend