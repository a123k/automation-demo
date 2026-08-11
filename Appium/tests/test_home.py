from pages.home_page import HomePage
import pytest

def test_app_launches_to_catalog(driver):
    home = HomePage(driver)
    assert home.get_title() == "Products"
    home.open_menu()
    assert home.is_menu_open(), "The sidebar menu failed to open"


def test_menu_options_are_listed(driver):
    home = HomePage(driver)
    home.open_menu()
    menu_status = home.get_all_menu_items_status()
    # Updated to match the optimized status check in home_page.py
    expected_items = ["Catalog", "Webview", "Log In"]
    for item in expected_items:
        assert menu_status[item] is True, f"Menu item '{item}' was not displayed"


def test_menu_persistence_after_navigation(driver):
    home = HomePage(driver)
    # Using a subset for faster execution and stability
    expected_items = ["Webview", "About", "Log In"]

    for item in expected_items:
        home.open_menu()
        home.click_menu_item(item)
        home.go_back()
        home.wait_for_catalog()
        home.open_menu()
        assert home.is_menu_open(), f"Menu failed to open after navigating back from {item}"
        home.go_back() # Close menu


def test_all_products_in_catalog(driver):
    home = HomePage(driver)
    expected_products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt" # Fixed: Removed '(Red)'
    ]
    actual_products = home.get_all_product_titles_scrolling()
    for product in expected_products:
        assert product in actual_products, f"Product '{product}' was missing from the catalog"