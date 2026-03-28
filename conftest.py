import pytest

from core.driver_factory import DriverFactory
from utils.screenshot import take_screenshot
from utils.logger import get_logger
from config.config_reader import ConfigReader


logger = get_logger(__name__)


@pytest.fixture(scope="function")
def driver():

    driver = None

    try:
        logger.info("Starting browser")

        driver = DriverFactory.get_driver()

        base_url = ConfigReader.get_base_url()

        logger.info(f"Opening URL: {base_url}")
        driver.get(base_url)

        yield driver

    finally:
        if driver:
            logger.info("Closing browser")
            driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            try:
                take_screenshot(driver, item.name)
            except Exception as e:
                logger.error(f"Screenshot failed: {e}")

        logger.error(f"Test failed: {item.name}")