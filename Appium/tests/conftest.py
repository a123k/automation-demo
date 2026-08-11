import pytest
import json
import os
import socket
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

def is_running_in_docker():
    """Checks if the script is running inside a Docker container."""
    path = '/proc/self/cgroup'
    return os.path.exists('/.dockerenv') or (os.path.isfile(path) and any('docker' in line for line in open(path)))

@pytest.fixture(scope="function")
def driver():
    # 1. Load defaults from config.json
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.json"))
    with open(config_path) as f:
        config = json.load(f)

    # 2. Smart Host Detection
    if is_running_in_docker():
        appium_url = "http://android-device:4723"
        app_path = "/app/Android-MyDemoAppRN.1.3.0.build-244.apk"
    else:
        # Running on host machine
        appium_url = "http://localhost:4723"
        # Try to find the APK in common locations on host
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        app_path = os.path.join(current_dir, "Android-MyDemoAppRN.1.3.0.build-244.apk")
        if not os.path.exists(app_path):
             app_path = "/home/aswathy/Downloads/Android-MyDemoAppRN.1.3.0.build-244.apk"

    options = UiAutomator2Options()
    options.platform_name = config.get("platform_name", "Android")
    options.automation_name = config.get("automation_name", "UiAutomator2")
    options.device_name = config.get("device_name", "Pixel_10")
    options.app = app_path
    options.app_package = "com.saucelabs.mydemoapp.rn"
    options.app_activity = ".MainActivity"

    options.no_reset = False
    options.auto_grant_permissions = True
    options.unicode_keyboard = True
    options.reset_keyboard = True
    options.set_capability("appium:disableWindowAnimation", True)

    print(f"Connecting to Appium at: {appium_url}")
    print(f"Using App Path: {app_path}")

    driver = webdriver.Remote(appium_url, options=options)

    # Stabilization
    import time
    time.sleep(5)

    # Handle initial popup
    try:
        wait = WebDriverWait(driver, 10)
        popup_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, "//*[@text='OK' or @text='ALLOW' or @text='ACCEPT']")
        ))
        popup_button.click()
    except TimeoutException:
        pass

    yield driver
    driver.quit()