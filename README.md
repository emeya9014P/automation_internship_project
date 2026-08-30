# 🚀 Python Selenium & API Test Automation Framework

Automated End-to-End (E2E) UI, API, Integration testing suite built with **Python**, **Selenium WebDriver**, and **Behave (BDD)** framework.

## 📌 Project Overview
This repository contains scalable test automation scripts designed for verifying complex web UI behaviors, RESTful API endpoints, dynamic element interactions, file upload/download flows, and cross-platform executions.

## ⚒️ Key Test Scenarios & Capabilities
- **BDD Architecture**: Feature-driven testing structure using Behave (Gherkin syntax: `Given`, `When`, `Then`).
- **Advanced UI Interactions**: Automated handling of dynamic iFrames, browser alerts, complex hover/drag actions using `ActionChains`, dropdown menus, and multi-window handle switching.
- **File I/O Verification**: Automated file upload execution and dynamic download directory verification strategies.
- **Cross-Browser & Cloud Testing**: Remote test execution configured for BrowserStack and headless browser modes.
- **Reporting & Emulation**: Test execution reports with Allure Framework and mobile web emulation setup.

## 💻 Tech Stack
- **Language**: Python 3
- **Automation Framework**: Selenium WebDriver, Behave (BDD)
- **Test Reporting**: Allure Framework
- **Cloud Infrastructure**: BrowserStack
- **Version Control & Tools**: Git, GitHub, PyCharm / VS Code

## 🧩 How to Run Tests
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
2. **Run all Behave scenarios**
   behave
3. **Generate Allure Report**
   behave -f allure_behave.formatter:AllureFormatter -o allure-results
   allure serve allure-results

## 🛠️ API Test Automation

Automated RESTful API test suite built with Python's `requests` library to validate core CRUD operations against the target endpoints.

### 🧪 Test Scenarios & Endpoints Covered

- **GET (`/api/users?page=2`)**
  - Validates HTTP `200 OK` status code.
  - Verifies page parameters and response array payload size.
- **POST (`/api/users`)**
  - Validates HTTP `201 Created` status code.
  - Asserts correct creation of new user entity and returned attributes (`name`, `job`, `id`).
- **PUT (`/api/users/2`)**
  - Validates HTTP `200 OK` status code.
  - Verifies successful update of existing user details.
- **DELETE (`/api/users/2`)**
  - Validates HTTP `204 No Content` status code confirming successful resource removal.

### 🧩 How to Run API Tests
1. **Install required dependencies**
   ```bash
   pip install requests
2. **Execute the test script**
   python test_api.py
   
## 🔄 CI/CD Pipeline (GitHub Actions)

- **Automated API & UI Testing**: Built a CI/CD automation pipeline using GitHub Actions to trigger test execution automatically upon every code push.
- **Headless Browser Execution**: Configured `features/environment.py` with environment detection (`os.getenv('CI')`) to automatically execute UI tests in `chrome_headless` mode within the CI server.
- **Module & Path Resolution**: Resolved `ModuleNotFoundError` in isolated CI runners by configuring `PYTHONPATH` and dynamically inserting the project root into `sys.path`.
- **Automated Regression Testing**: Ensured code quality and prevented regression defects by validating existing test suites on clean virtual runners before merging.
- **Automated Test Reporting**: Generated and automatically deployed interactive Allure Test Reports to GitHub Pages to track test pass/fail metrics and execution history.
