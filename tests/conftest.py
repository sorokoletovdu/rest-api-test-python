import pytest
from helpers.api_helper import APIClient


@pytest.fixture
def api_client():
    return APIClient(base_url="https://api.test.idnow.de/api/v1")
