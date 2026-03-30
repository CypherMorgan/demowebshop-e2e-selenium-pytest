import pytest
from utils.api_client import APIClient


@pytest.fixture
def client():
    return APIClient("https://fakestoreapi.com")


@pytest.mark.api
@pytest.mark.smoke
def test_login_success(client):
    response = client.post("/auth/login", json={
        "username": "mor_2314",
        "password": "83r5^_"
    })

    assert response.status_code in [200, 201]
    assert "token" in response.json()


@pytest.mark.api
def test_login_invalid(client):
    response = client.post("/auth/login", json={
        "username": "wrong",
        "password": "wrong"
    })

    assert response.status_code in [400, 401]