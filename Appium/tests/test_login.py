import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def navigate_to_login(driver):
    home = HomePage(driver)
    home.open_menu()
    home.click_menu_item("Log In")
    return LoginPage(driver)


def test_successful_login(navigate_to_login, driver):
    login_page = navigate_to_login
    login_page.login("bob@example.com", "10203040")
    home = HomePage(driver)
    assert home.get_title() == "Products", "Login failed: Not redirected to Products"


def test_login_invalid_credentials(navigate_to_login):
    login_page = navigate_to_login
    login_page.login("wrong@example.com", "wrongpass")
    error = login_page.get_error_text()
    assert "Provided credentials do not match" in error


def test_login_locked_out_user(navigate_to_login):
    login_page = navigate_to_login
    login_page.login("alice@example.com", "10203040")
    error = login_page.get_error_text()
    assert "Sorry, this user has been locked out" in error


def test_login_empty_username(navigate_to_login):
    login_page = navigate_to_login
    login_page.login("", "10203040")
    error = login_page.get_error_text()
    assert "Username is required" in error


def test_login_empty_password(navigate_to_login):
    login_page = navigate_to_login
    login_page.login("bob@example.com", "")
    error = login_page.get_error_text()
    assert "Password is required" in error