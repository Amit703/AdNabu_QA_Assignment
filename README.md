# AbNabu_QA_Assignment
Task 1: Test Design
● Write 6 high-quality test cases for a) Product Search and b) Add to Cart
- Requirements: 1. Must include positive + negative cases
2. Must include at least 1 edge case 3. Keep it concise and mention the expected result clearly (You may use bullets)
Task 2: Test Automation
● Automate only one scenario: Search for a product and add it to the cart successfully
- Requirements: 1. Use Python + Selenium 2. No hardcoded sleeps (use proper waits)
3. Code must be readable and modular
- You DO NOT need to 1. Set-up full framework 2. Add cross-browser support 3. Add reporting tool 4. Cover all scenarios


Automation Framework Setup & Execution Guide
Project Overview

This project is a Selenium automation framework developed using Python, Pytest, and Selenium WebDriver.

1) The framework includes:

Selenium test scripts
HTML test reporting
Pytest execution support
Easy project setup and execution

2) Prerequisites

Ensure the following software is installed on your system:

Python 3.x
Google Chrome browser
PyCharm or any IDE

3) Install Dependencies

pip install -r requirements.txt

4) Run Automated Tests
pytest tests/test_login.py

5) Generate HTML Report

pytest tests/test_login.py --html=reports/report.html --self-contained-html
