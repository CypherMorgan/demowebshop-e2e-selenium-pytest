import pytest
from utils.api_client import APIClient
from config.config_reader import ConfigReader


@pytest.fixture
def client():
    return APIClient(ConfigReader.get_api_base_url())


@pytest.mark.api
@pytest.mark.smoke
def test_login_success(client):
    if "httpbin" in client.base_url:
        response = client.post("/post", json={"test": "data"})
        assert response.status_code == 200
    else:
        response = client.post("/auth/login", json={
            "username": "mor_2314",
            "password": "83r5^_"
        })
        assert response.status_code in [200, 201]
        assert "token" in response.json()