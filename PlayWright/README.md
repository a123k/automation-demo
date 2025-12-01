# Playwright TypeScript Project

This project is a **Playwright test automation framework** built with **TypeScript** and designed to run in **VS Code**. It includes best practices for writing maintainable end-to-end (E2E) tests. Sample site used in this framework is https://www.saucedemo.com/

---

## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Project Structure](#project-structure)
* [Running Tests](#running-tests)
* [Configuration](#configuration)
* [Writing Tests](#writing-tests)
* [Assertions and Locators](#assertions-and-locators)
* [Reporting](#reporting)
* [Tips for VS Code](#tips-for-vs-code)

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
git clone https://github.com/your-repo/playwright-ts-project.git
cd playwright-ts-project
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

---

## Project Structure

```
playwright-ts-project/
## Project Structure

```
PLAYWRIGHT/
│
├─ env/                   # Environment files
│   ├─ .env.prod
│   └─ .env.staging
│
├─ node_modules/           # Node.js dependencies
│
├─ reports/                # Cucumber and test reports
│   └─ cucumber.json
│
├─ src/                    # Source code
│   ├─ hooks/              # Hooks and custom world for Cucumber
│   │   ├─ hooks.ts
│   │   └─ world.ts
│   │
│   ├─ pages/              # Page Object Model classes
│   │   ├─ LoginPage.ts
│   │   └─ ProductPage.ts
│   │
│   └─ test/               # Test files (step definitions or specs)
│
├─ test-results/           # Test execution results
│
├─ .gitignore
├─ cucumber.json           # Cucumber configuration
├─ package-lock.json
├─ package.json
├─ README.md
└─ tsconfig.json           # TypeScript configuration
```

```

---

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

Playwright provides built-in reports:

* HTML report:

```bash
npx playwright show-report
```

* Enable in `playwright.config.ts`:

```ts
reporter: [['list'], ['html']],
```

---

## References

* [Playwright Docs](https://playwright.dev/)
* [Playwright TypeScript](https://playwright.dev/docs/intro)
* [Cucumber BDD](https://cucumber.io/docs/)

---

This setup ensures **scalable, maintainable, and readable E2E tests** in TypeScript using Playwright and VS Code.
