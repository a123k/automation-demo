from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    # Address Fields
    FULL_NAME = (AppiumBy.ACCESSIBILITY_ID, "Full Name* input field")
    ADDRESS_LINE_1 = (AppiumBy.ACCESSIBILITY_ID, "Address Line 1* input field")
    CITY = (AppiumBy.ACCESSIBILITY_ID, "City* input field")
    ZIP_CODE = (AppiumBy.ACCESSIBILITY_ID, "Zip Code* input field")
    COUNTRY = (AppiumBy.ACCESSIBILITY_ID, "Country* input field")

    # Payment Fields (Note: often reuse descriptors in this app)
    CARD_NUMBER = (AppiumBy.ACCESSIBILITY_ID, "Card Number* input field")
    EXPIRY_DATE = (AppiumBy.ACCESSIBILITY_ID, "Expiration Date* input field")
    SECURITY_CODE = (AppiumBy.ACCESSIBILITY_ID, "Security Code* input field")

    # Buttons
    TO_PAYMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "To Payment button")
    REVIEW_ORDER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Review Order button")
    PLACE_ORDER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Place Order button")

    # Success Screen
    CHECKOUT_COMPLETE_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Checkout Complete")')

    # Error Locators
    ERROR_MESSAGE = (AppiumBy.XPATH, "//*[contains(@text, 'required') or contains(@text, 'invalid') or contains(@text, 'Short') or contains(@text, 'match')]")

    def fill_shipping_address(self, name="", address="", city="", zip_code="", country=""):
        self.send_keys(self.FULL_NAME, name)
        self.send_keys(self.ADDRESS_LINE_1, address)
        self.scroll_down() # Ensure the rest of the form is visible
        self.send_keys(self.CITY, city)
        self.send_keys(self.ZIP_CODE, zip_code)
        self.send_keys(self.COUNTRY, country)
        self.click(self.TO_PAYMENT_BUTTON)
        time.sleep(2) # Screen transition

    def fill_payment_details(self, name="", card_no="", expiry="", cvv=""):
        # The 'Full Name' field on Payment screen often shares ID with Address screen
        # Use XPATH to target the last (current) one if needed, but ACCESSIBILITY_ID usually works if screen refreshed
        name_field = (AppiumBy.XPATH, "(//android.widget.EditText[@content-desc='Full Name* input field'])[last()]")
        self.send_keys(name_field, name)
        self.send_keys(self.CARD_NUMBER, card_no)
        self.scroll_down()
        self.send_keys(self.EXPIRY_DATE, expiry)
        self.send_keys(self.SECURITY_CODE, cvv)
        self.click(self.REVIEW_ORDER_BUTTON)
        time.sleep(2)

    def place_order(self):
        self.scroll_to_text("Place Order")
        self.click(self.PLACE_ORDER_BUTTON)

    def is_checkout_complete(self):
        return self.is_element_displayed(self.CHECKOUT_COMPLETE_TITLE, timeout=10)

    def get_success_message(self):
        return self.find_element(self.CHECKOUT_COMPLETE_TITLE).text

    def get_validation_errors(self):
        # Don't use find_element (which has retry-scroll) here to avoid false positives
        return [el.text for el in self.driver.find_elements(*self.ERROR_MESSAGE)]