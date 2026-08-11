from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from appium.webdriver.common.appiumby import AppiumBy

def test_successful_product_order_e2e(driver):
    home = HomePage(driver)

    # 1. Select a product
    product_name = "Sauce Labs Backpack"
    home.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{product_name}")'))

    # 2. Add to cart
    product_details = ProductDetailsPage(driver)
    product_details.add_to_cart()

    # 3. Go to cart and proceed
    home.open_cart()
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    # 4. Login (Required for checkout)
    login = LoginPage(driver)
    login.login("bob@example.com", "10203040")

    # 5. Fill Shipping Address
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_address(
        name="Bob Demo",
        address="123 Appium Street",
        city="London",
        zip_code="SW1 1AA",
        country="United Kingdom"
    )

    # 6. Fill Payment Details (Valid 16-digit Visa)
    checkout.fill_payment_details(
        name="Bob Demo",
        card_no="4111111111111111",
        expiry="12/28",
        cvv="123"
    )

    # 7. Review and Place Order
    checkout.place_order()

    # 8. Assertion: Verify Order Success
    assert checkout.is_checkout_complete(), "Checkout was not completed successfully"
    assert checkout.get_success_message() == "Checkout Complete", "Success message mismatch"
