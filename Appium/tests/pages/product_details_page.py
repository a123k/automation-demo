from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")

    def add_to_cart(self):
        # Try to find the button, if not visible, scroll
        try:
            self.click(self.ADD_TO_CART_BUTTON)
        except:
            self.scroll_to_text("Add To Cart")
            self.click(self.ADD_TO_CART_BUTTON)