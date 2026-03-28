from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchPage(BasePage):

    PRODUCT_LINK = (By.CSS_SELECTOR, ".product-title a")

    def open_first_product(self):

        self.wait.until(EC.presence_of_element_located(self.PRODUCT_LINK))

        for _ in range(2):
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(self.PRODUCT_LINK)
                )
                element.click()
                return
            except Exception:
                continue

        raise Exception("Failed to click product (stale element)")