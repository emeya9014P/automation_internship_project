# 🚀 Python Selenium BDD Test Automation Framework

Automated End-to-End (E2E) UI & Integration testing suite built with **Python**, **Selenium WebDriver**, and **Behave (BDD)** framework.

## 📌 Project Overview
This repository contains scalable test automation scripts designed for verifying complex web behaviors, dynamic UI interactions, file upload/download flows, and cross-platform executions.

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
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
2. **Run all Behave scenarios**:
   behave
3. **Generate Allure Report**:
   behave -f allure_behave.formatter:AllureFormatter -o allure-results
   allure serve allure-results
   
