from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    StaleElementReferenceException,
    TimeoutException
)
from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_LINK = (By.CSS_SELECTOR, ".cart-label")

    def add_to_cart(self):

        self.wait.until(EC.presence_of_element_located(self.ADD_TO_CART_BUTTON))

        for _ in range(2):
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
                )
                element.click()

                try:
                    alert = self.driver.switch_to.alert
                    print(f"Alert detected: {alert.text}")
                    alert.accept()
                except:
                    pass

                return

            except (UnexpectedAlertPresentException, StaleElementReferenceException, TimeoutException):
                continue

        raise Exception("Failed to add product to cart after retries")

    def go_to_cart(self):
        self.click(self.CART_LINK)