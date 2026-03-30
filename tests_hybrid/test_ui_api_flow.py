import pytest
from utils.api_client import APIClient
from config.config_reader import ConfigReader


@pytest.mark.hybrid
@pytest.mark.smoke
def test_product_visible_api_ui(driver):
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products/1")
    assert response.status_code == 200

    data = response.json()
    product_title = data.get("title")

    assert product_title and isinstance(product_title, str)

    driver.get(ConfigReader.get_base_url())

    assert "demo web shop" in driver.title.lower()