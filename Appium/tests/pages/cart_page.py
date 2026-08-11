from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    REMOVE_ITEM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "remove item")
    PROCEED_TO_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, "Proceed To Checkout button")
    EMPTY_CART_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("cart is empty")')

    def remove_item(self):
        self.click(self.REMOVE_ITEM_BUTTON)
        time.sleep(1) # Allow item to disappear

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)

    def is_cart_empty(self):
        return self.is_element_displayed(self.EMPTY_CART_MESSAGE, timeout=15)