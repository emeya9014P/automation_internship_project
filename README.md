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
   
