# Selenium Automation Framework (Python)

## What is this
Simple Selenium Page Object Model sample using pytest and webdriver-manager.
It runs tests against the public demo site: https://the-internet.herokuapp.com/login

## How to run locally
1. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run tests
   ```bash
   pytest
   ```
3. HTML report will be saved in `reports/report.html`

## Files
- pages/: Page Object classes
- tests/: pytest test files
- conftest.py: pytest fixtures for webdriver
- pytest.ini: pytest config
