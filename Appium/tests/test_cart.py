from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from appium.webdriver.common.appiumby import AppiumBy


def test_add_and_remove_from_cart(driver):
    home = HomePage(driver)
    # 1. Select a product (Sauce Labs Backpack)
    product_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sauce Labs Backpack")')
    home.click(product_locator)
    # 2. Add to Cart
    product_details = ProductDetailsPage(driver)
    product_details.add_to_cart()
    # 3. Assertion: Verify Cart Badge shows 1
    assert home.get_cart_count() == 1, "Cart badge count did not increase to 1"
    # 4. Navigate to Cart
    home.open_cart()
    cart = CartPage(driver)
    # 5. Remove Item
    cart.remove_item()
    # 6. Assertion: Verify Cart is empty
    assert cart.is_cart_empty(), "Cart was not empty after removing the item"
    assert home.get_cart_count() == 0, "Cart badge still shows items after removal"