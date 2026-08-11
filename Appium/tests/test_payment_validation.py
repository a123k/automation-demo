from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from appium.webdriver.common.appiumby import AppiumBy

def test_payment_validation_blocks_order_review(driver):
    home = HomePage(driver)

    # 1. Setup
    home.click((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sauce Labs Backpack")'))
    ProductDetailsPage(driver).add_to_cart()
    home.open_cart()
    CartPage(driver).proceed_to_checkout()
    LoginPage(driver).login("bob@example.com", "10203040")
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_address("Bob", "123 St", "London", "SW1", "UK")
    # 2. Enter INVALID payment data
    checkout.fill_payment_details(name="", card_no="1234", expiry="01/20", cvv="1")
    # 3. Assertions
    assert driver.find_element(*checkout.REVIEW_ORDER_BUTTON).is_displayed()
    errors = checkout.get_validation_errors()
    assert len(errors) > 0