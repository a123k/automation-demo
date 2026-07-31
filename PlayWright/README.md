# Playwright TypeScript Project

This project is a **Playwright test automation framework** built with **TypeScript** and designed to run in **VS Code**. It includes best practices for writing maintainable end-to-end (E2E) tests. Sample site used in this framework is https://www.saucedemo.com/

---

## Prerequisites

* Node.js >= 18
* npm or yarn
* VS Code (recommended)
* Playwright installed globally or locally in the project

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/a123k/automation-demo.git
cd PlayWright
```

2. Install dependencies:

```bash
npm install
# or
yarn install
```

3. Install Playwright browsers:

```bash
npx playwright install
```

## Running Tests

### Run all tests

```bash
ENV=staging npm run test
```
### Run a specific tag

```bash
ENV=staging npm run test:tag -- '@TC-1'
```

### Run tests in headless mode 

```bash
ENV=staging HEADLESS=true npm run test
```

### Run tests in a specific browser

```bash
ENV=staging BROWSER=firefox npm run test 
```

## Reporting

* Allure report:

```bash
npm run allure:report
```
```bash
npm run allure:open
```

## References

* [Playwright Docs](https://playwright.dev/)
* [Playwright TypeScript](https://playwright.dev/docs/intro)
* [Cucumber BDD](https://cucumber.io/docs/)

---

This setup ensures **scalable, maintainable, and readable E2E tests** in TypeScript using Playwright and VS Code.
