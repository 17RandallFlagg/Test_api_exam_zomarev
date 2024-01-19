import pytest
import requests_list


@pytest.fixture(scope="function")
def api_client(request):
    base_url = getattr(request.cls, "base_url", "")
    return ApiClient(base_url)
