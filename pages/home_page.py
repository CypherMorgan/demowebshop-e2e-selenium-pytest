from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")

    def go_to_register(self):
        self.click(self.REGISTER_LINK)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def search_product(self, product):
        self.type(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BUTTON)
