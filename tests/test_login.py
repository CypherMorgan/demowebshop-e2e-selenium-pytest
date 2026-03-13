import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.config_reader import ConfigReader
from utils.logger import get_logger


logger = get_logger(__name__)


@allure.feature("Authentication")
@allure.story("User Login")
def test_login(driver):

    logger.info("Starting login test")

    home = HomePage(driver)

    logger.info("Navigating to login page")
    home.go_to_login()

    login = LoginPage(driver)

    username = ConfigReader.get_username()
    password = ConfigReader.get_password()

    logger.info(f"Logging in with user: {username}")

    login.login(username, password)

    logger.info("Verifying login success")

    assert login.is_logged_in()

    logger.info("Login test passed")
