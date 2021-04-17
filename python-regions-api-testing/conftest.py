import pytest
from src.client import ApiClient



@pytest.fixture
def regions_api():
    return ApiClient("https://regions-test.2gis.com/1.0/regions")