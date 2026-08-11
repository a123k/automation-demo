from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")

    # Updated locator to match various error texts in the demo app
    ERROR_MESSAGE = (AppiumBy.XPATH, "//*[contains(@text, 'required') or contains(@text, 'match') or contains(@text, 'locked')]")

    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_text(self):
        # We use a short wait here as errors appear immediately after click
        return self.find_element(self.ERROR_MESSAGE).text