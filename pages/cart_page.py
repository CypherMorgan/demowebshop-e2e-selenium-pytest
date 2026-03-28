from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):

        self.wait.until(EC.presence_of_element_located(self.TERMS_CHECKBOX))

        self.wait.until(EC.url_contains("cart"))

        self.wait.until(EC.element_to_be_clickable(self.TERMS_CHECKBOX)).click()

        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()