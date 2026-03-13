from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT = (By.CLASS_NAME, "ico-logout")

    @allure.step("Login with email: {email}")
    def login(self, email, password):

        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        return self.is_visible(self.LOGOUT)
