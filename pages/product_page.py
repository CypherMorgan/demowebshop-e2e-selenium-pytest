from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")
    CART_LINK = (By.CSS_SELECTOR, "span.cart-label")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_LINK)