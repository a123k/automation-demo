from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        """Finds an element with an implicit scroll retry if not found."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            # Try to scroll down and find again
            self.scroll_down()
            return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Clicks an element, scrolling to it if necessary."""
        try:
            el = self.wait.until(EC.element_to_be_clickable(locator))
            el.click()
        except:
            # If not clickable, maybe it's off-screen or behind keyboard
            self.hide_keyboard()
            self.scroll_down()
            el = self.wait.until(EC.element_to_be_clickable(locator))
            el.click()

    def hide_keyboard(self):
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except:
            pass

    def send_keys(self, locator, text):
        """Clears and sends keys to an element, ensuring keyboard is hidden after."""
        el = self.find_element(locator)
        el.clear()
        el.send_keys(text)
        self.hide_keyboard()

    def go_back(self):
        self.driver.back()
        time.sleep(1)

    def scroll_to_text(self, text):
        """Native Android scroll to text."""
        try:
            return self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{text}"))'
            )
        except Exception:
            # Manual fallback for stubborn views
            for _ in range(3):
                try:
                    return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
                except:
                    self.scroll_down()
            raise

    def scroll_down(self):
        """Perform a smaller, more controlled scroll down."""
        size = self.driver.get_window_size()
        # Swipe from middle-bottom to middle-top
        self.driver.swipe(size['width']/2, size['height']*0.7, size['width']/2, size['height']*0.4, 600)
        time.sleep(1)

    def is_element_displayed(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False