from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException, StaleElementReferenceException
from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_LINK = (By.CSS_SELECTOR, ".cart-label")

    def add_to_cart(self):

        for _ in range(2):
            try:
                self.click(self.ADD_TO_CART_BUTTON)

                try:
                    alert = self.driver.switch_to.alert
                    print(f"Alert detected: {alert.text}")
                    alert.accept()
                except:
                    pass

                return

            except (UnexpectedAlertPresentException, StaleElementReferenceException):
                continue

        raise Exception("Failed to add product to cart after retries")

    def go_to_cart(self):
        self.click(self.CART_LINK)