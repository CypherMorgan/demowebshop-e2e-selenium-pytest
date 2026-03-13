from pages.home_page import HomePage
from pages.register_page import RegisterPage, generate_email


def test_register(driver):

    home = HomePage(driver)
    home.go_to_register()

    register = RegisterPage(driver)

    email = generate_email()

    register.register_user(
        "John",
        "Doe",
        email,
        "Password123"
    )

    assert "completed" in register.get_success_message().lower()
