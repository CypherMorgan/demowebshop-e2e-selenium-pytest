from selenium import webdriver
from config.config_reader import ConfigReader
import os


class DriverFactory:

    @staticmethod
    def get_driver():

        browser = ConfigReader.get_browser().lower()
        headless = ConfigReader.is_headless()

        is_ci = os.getenv("CI") == "true"

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if headless or is_ci:
                options.add_argument("--headless=new")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            if headless or is_ci:
                options.add_argument("--headless")

            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            driver = webdriver.Firefox(options=options)

        else:
            raise Exception(f"Unsupported browser: {browser}")

        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        return driver