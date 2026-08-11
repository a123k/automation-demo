from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from appium.webdriver.common.appiumby import AppiumBy

def test_checkout_validation_blocks_payment(driver):
    home = HomePage(driver)

    # 1. Add item
    home.click((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sauce Labs Backpack")'))
    product_details = ProductDetailsPage(driver)
    product_details.add_to_cart()
    home.open_cart()
    cart = CartPage(driver)
    cart.proceed_to_checkout()
    # 2. Login
    login = LoginPage(driver)
    login.login("bob@example.com", "10203040")
    # 3. Enter INVALID address data
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_address(name="", address="", city="", zip_code="invalid")
    # 4. Assertions
    assert driver.find_element(*checkout.TO_PAYMENT_BUTTON).is_displayed()
    errors = checkout.get_validation_errors()
    assert len(errors) > 0