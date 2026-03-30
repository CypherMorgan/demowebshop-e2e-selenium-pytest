import pytest
from utils.api_client import APIClient
from config.config_reader import ConfigReader


@pytest.mark.hybrid
@pytest.mark.smoke
def test_product_visible_api_ui(driver):
    client = APIClient(ConfigReader.get_api_base_url())

    response = client.get("/products/1" if "fakestore" in client.base_url else "/get")

    assert response.status_code == 200

    driver.get(ConfigReader.get_base_url())

    assert "demo web shop" in driver.title.lower()