from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from pages.base_page import BasePage


class SearchPage(BasePage):

    PRODUCT_LINK = (By.CSS_SELECTOR, ".product-title a")

    def open_first_product(self):

        for _ in range(3):
            try:
                elements = self.wait.until(
                    EC.presence_of_all_elements_located(self.PRODUCT_LINK)
                )

                element = elements[0]

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", element
                )

                import time
                time.sleep(1)

                self.driver.execute_script("arguments[0].click();", element)

                self.wait.until(
                    lambda d: "product" in d.current_url
                    or len(d.find_elements(By.CSS_SELECTOR, ".product-name")) > 0
                )

                return

            except (StaleElementReferenceException, TimeoutException):
                continue

    raise Exception("Failed to open product page")