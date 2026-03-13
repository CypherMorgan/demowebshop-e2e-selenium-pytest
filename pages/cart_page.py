from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BTN = (By.ID, "checkout")

    def checkout(self):

        self.click(self.TERMS_CHECKBOX)
        self.click(self.CHECKOUT_BTN)
