from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class HomePage(BasePage):
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    CATALOG_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Products")')
    LOG_IN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")

    # Menu Items
    CATALOG_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item catalog")
    WEBVIEW_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item webview")
    QR_CODE_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item qr code scanner")
    GEO_LOCATION_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item geo location")
    DRAWING_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item drawing")
    ABOUT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item about")
    LOG_IN_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")

    # Products
    PRODUCT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "store item")
    PRODUCT_TITLE = (AppiumBy.ACCESSIBILITY_ID, "store item text")
    PRODUCT_PRICE = (AppiumBy.ACCESSIBILITY_ID, "store item price")

    # Cart
    CART_BADGE = (AppiumBy.ACCESSIBILITY_ID, "cart badge")

    def open_menu(self):
        self.click(self.MENU_BUTTON)
        time.sleep(1)

    def get_title(self):
        return self.find_element(self.CATALOG_TITLE).text

    def is_menu_open(self):
        return self.is_element_displayed(self.LOG_IN_MENU_ITEM)

    def click_menu_item(self, item_name):
        locators = {
            "Catalog": self.CATALOG_ITEM, "Webview": self.WEBVIEW_ITEM, "QR Code": self.QR_CODE_ITEM,
            "Geo Location": self.GEO_LOCATION_ITEM, "Drawing": self.DRAWING_ITEM, "About": self.ABOUT_ITEM,
            "Log In": self.LOG_IN_ITEM
        }
        self.click(locators[item_name])

    def get_all_menu_items_status(self):
        items = ["Catalog", "Webview", "Log In"]
        locators = {"Catalog": self.CATALOG_ITEM, "Webview": self.WEBVIEW_ITEM, "Log In": self.LOG_IN_ITEM}
        return {item: self.is_element_displayed(locators[item], timeout=2) for item in items}

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEM))

    def get_all_product_titles(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_TITLE)]

    def get_all_product_titles_scrolling(self):
        all_titles = set()
        last_count = -1
        for _ in range(5):
            titles = self.get_all_product_titles()
            all_titles.update(titles)
            if len(all_titles) == last_count: break
            last_count = len(all_titles)
            self.scroll_down()
            time.sleep(1)
        return list(all_titles)

    def get_cart_count(self):
        time.sleep(1)
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            text_el = badge.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView")')
            return int(text_el.text)
        except:
            return 0

    def open_cart(self):
        self.click(self.CART_BADGE)

    def wait_for_catalog(self):
        # Retry with a back button if the title isn't found
        for _ in range(2):
            try:
                return self.find_element(self.CATALOG_TITLE)
            except:
                self.go_back()
        raise TimeoutException("Catalog screen did not appear")