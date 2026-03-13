from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from config.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        browser = ConfigReader.get_browser()
        headless = ConfigReader.is_headless()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser == "firefox":

            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )

        else:
            raise Exception("Unsupported browser")

        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        return driver
