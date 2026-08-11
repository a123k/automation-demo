# Appium Android Automation Framework

A robust, scalable mobile automation framework for the **Sauce Labs My Demo App (React Native)** using Python, Pytest, and the Page Object Model (POM) design pattern.

## 🚀 Features
- **Page Object Model (POM):** Decoupled locators and test logic for high maintainability.
- **Robust Locators:** Optimized XPATH, Accessibility IDs, and Android UiAutomator selectors for React Native stability.
- **Auto-Scrolling:** Smart scrolling logic using `UiScrollable` to handle dynamic content.
- **Session Isolation:** Each test starts with a clean app state (`noReset=False`).
- **E2E Coverage:** Complete flows from login to successful order placement.
- **External Configuration:** Manage APK paths and device names via `config.json`.
- **Automated Reporting:** Generates self-contained HTML reports after every run.

---

## 🛠️ Prerequisites
- **Python 3.10+**
- **Android SDK:** Installed and configured in environment variables.
- **Appium Server 2.x/3.x:** Installed via NPM.
- **UiAutomator2 Driver:** `appium driver install uiautomator2`
- **Android Emulator:** Recommended device `Pixel_10` with Android 17 (API 37).
- **Demo APK:** Download the latest Android release from [Sauce Labs My Demo App GitHub](https://github.com/saucelabs/my-demo-app-rn/releases).

---

## 📦 Setup & Installation

### 1. Environment Variables
Ensure your `~/.bashrc` or `~/.zshrc` includes:
```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### 2. Virtual Environment
```bash
cd Appium/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration
Copy `config.json` and update the `app_path` to your local APK location:
```json
{
  "app_path": "/path/to/your/Android-MyDemoAppRN.apk",
  "appium_server_url": "http://localhost:4723",
  "device_name": "Pixel_10"
}
```

---

## 🏃 Running Tests Locally

### Start the Appium Server
Open a terminal and run: `appium`

### Execute Tests with Reporting
```bash
python -m pytest tests/ -v --html=reports/report.html --self-contained-html
```

---

## 🐳 Running with Docker

### 1. Prepare the APK
Move your APK into the `Appium/` directory: `cp ~/Downloads/Android-MyDemoAppRN.apk .`

### 2. Update config.json for Docker
```json
{
  "app_path": "/app/Android-MyDemoAppRN.1.3.0.build-244.apk",
  "appium_server_url": "http://android-device:4723",
  "device_name": "Samsung Galaxy S10"
}
```

### 3. Build and Run
```bash
docker-compose up --build
```
*You can view the live emulator screen at `http://localhost:6080`*

---

## 📊 Accessing Reports

Regardless of whether you run locally or via Docker, the reports are accessed the same way:

1.  Navigate to the `Appium/reports/` folder in your file explorer.
2.  Open **`report.html`** in any web browser.
3.  The report includes execution time, pass/fail status, and detailed error logs for failures.

---

## 📂 Project Structure
```text
Appium/
├── tests/
│   ├── conftest.py          # Driver setup & Smart Host Detection
│   ├── pages/               # Page Object Model implementations
│   └── test_*.py            # Functional test suites
├── reports/                 # Generated HTML reports
├── config.json              # Configuration for different environments
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## 🧪 Test Coverage
1. **Login:** Success, Invalid Credentials, Locked Out, Empty Fields.
2. **Catalog:** Product details and full catalog scrolling verification.
3. **Cart:** Add/Remove functionality and Badge synchronization.
4. **Checkout:** Address and Payment form validations.
5. **End-to-End:** Complete purchase journey to "Checkout Complete".
