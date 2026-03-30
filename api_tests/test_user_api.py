import pytest
from utils.api_client import APIClient
from config.config_reader import ConfigReader


@pytest.fixture
def client():
    return APIClient(ConfigReader.get_api_base_url())


@pytest.mark.api
@pytest.mark.smoke
def test_get_products(client):
    if "httpbin" in client.base_url:
        response = client.get("/get")
        assert response.status_code == 200
    else:
        response = client.get("/products")
        assert response.status_code == 200
        assert isinstance(response.json(), list)