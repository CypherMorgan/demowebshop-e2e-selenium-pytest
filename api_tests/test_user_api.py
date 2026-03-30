import pytest
from utils.api_client import APIClient


@pytest.fixture
def client():
    return APIClient("https://fakestoreapi.com")


@pytest.mark.api
@pytest.mark.smoke
def test_get_products(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.api
def test_get_single_product(client):
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1