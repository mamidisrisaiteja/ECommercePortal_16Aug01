# Test Automation Framework

[![Regression Tests](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/workflows/Regression%20Test%20Pipeline/badge.svg)](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/actions)
[![Smoke Tests](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/workflows/Smoke%20Tests/badge.svg)](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/actions)
[![Release](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/workflows/Release%20Pipeline/badge.svg)](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/releases)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/playwright-1.40.0-green.svg)](https://playwright.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive BDD test automation framework built with Python, Playwright, Pytest, and Cucumber for testing the SauceDemo e-commerce application.

## Framework Features

- **BDD (Behavior Driven Development)** with Gherkin syntax
- **Page Object Model** design pattern
- **Playwright** for browser automation
- **Pytest** as the test runner
- **Pytest-BDD** for BDD implementation
- **Cross-browser testing** (Chromium, Firefox, WebKit)
- **Parallel test execution**
- **HTML and Allure reporting**
- **Screenshot capture on failure**
- **Video recording** (optional)
- **Configurable test environments**
- **Comprehensive logging**

## Project Structure

```
automation_framework/
├── config/                     # Configuration files
│   ├── config.py              # Configuration management
│   └── default.yaml           # Default configuration
├── fixtures/                   # Pytest fixtures
│   └── browser_fixtures.py    # Browser and page fixtures
├── pages/                      # Page Object Model
│   ├── base_page.py           # Base page class
│   ├── login_page.py          # Login page object
│   ├── products_page.py       # Products page object
│   └── cart_page.py           # Cart page object
├── tests/                      # Test files
│   ├── features/              # BDD feature files
│   │   ├── authentication.feature
│   │   ├── inventory.feature
│   │   └── cart.feature
│   ├── step_definitions/      # Step definition files
│   │   └── test_steps.py
│   └── conftest.py           # Pytest configuration
├── utils/                      # Utility modules
│   ├── logger.py              # Logging utility
│   └── helpers.py             # Helper functions
├── reports/                    # Test reports and artifacts
│   ├── screenshots/           # Screenshot storage
│   ├── videos/               # Video recordings
│   ├── logs/                 # Test execution logs
│   └── allure-results/       # Allure test results
├── requirements.txt           # Python dependencies
├── pytest.ini               # Pytest configuration
└── README.md                # This file
```

## Test Cases Implemented

### Authentication Module (@auth)
- **TC_AUTH_01**: Login with valid credentials (@smoke)
- **TC_AUTH_02**: Login with invalid credentials (@regression)

## Quick Start with Makefile

### Using Make Commands (Recommended)
```bash
# Setup everything
make setup

# Run authentication tests
make test-auth

# Run smoke tests
make test-smoke

# Run regression tests  
make test-regression

# Run tests with visible browser
make test-headed

# Generate reports
make reports

# Clean reports
make clean
```

## Installation and Setup

1. **Clone the repository**
   ```bash
   cd automation_framework
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test by tag
```bash
# Run only authentication tests
pytest -m auth

# Run only inventory tests  
pytest -m inventory

# Run only cart tests
pytest -m cart

# Run smoke tests
pytest -m smoke

# Run regression tests
pytest -m regression
```

### Run specific test case
```bash
# Run specific test case by ID
pytest -k "TC_AUTH_01"
pytest -k "TC_AUTH_02"
```

### Run tests in parallel
```bash
pytest -n auto
```

### Run tests with different browsers
```bash
# Chromium (default)
pytest --browser=chromium

# Firefox
pytest --browser=firefox

# WebKit
pytest --browser=webkit
```

### Run tests in headless mode
```bash
pytest --browser=chromium --headed=false
```

## Configuration

### Environment Variables
- `BASE_URL`: Override base URL (default: https://www.saucedemo.com)
- `BROWSER_NAME`: Browser to use (chromium, firefox, webkit)
- `HEADLESS`: Run in headless mode (true/false)
- `TEST_ENV`: Test environment (default, staging, prod)

### Configuration Files
Edit `config/default.yaml` to modify:
- Browser settings
- Timeouts
- Test data
- Screenshot settings

## Reporting

### HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report
```bash
# Generate Allure results
pytest --alluredir=reports/allure-results

# Serve Allure report
allure serve reports/allure-results
```

## Test Data

Test data is managed through:
- Configuration files (`config/default.yaml`)
- Environment variables
- Direct parameterization in feature files

## Page Objects

All page objects inherit from `BasePage` which provides:
- Common web element interactions
- Wait strategies
- Screenshot capabilities
- Logging functionality

## Logging

- Logs are stored in `reports/logs/`
- Console and file logging
- Different log levels (INFO, ERROR, DEBUG)
- Automatic log rotation

## Screenshots

- Automatic screenshot on test failure
- Manual screenshot capability
- Stored in `reports/screenshots/`
- Timestamped filenames

## Video Recording

Enable video recording by setting in configuration:
```yaml
record_video: true
```

Videos are stored in `reports/videos/`

## CI/CD Pipeline

This framework includes comprehensive CI/CD pipelines with GitHub Actions:

### 🚀 **Automated Pipelines:**

1. **Regression Test Pipeline**
   - Triggers: Push to main/develop, PRs, daily schedule
   - Features: Multi-browser, multi-Python version testing
   - Reports: HTML, Allure, JUnit with GitHub Pages deployment

2. **Smoke Test Pipeline**
   - Triggers: Push to main, PRs
   - Features: Quick validation with TC_AUTH_01
   - Duration: ~2 minutes for fast feedback

3. **Release Pipeline**
   - Triggers: Git tags (v*.*.*)
   - Features: Full test suite, automated releases
   - Artifacts: Framework archive, release notes

### 📊 **Live Reports:**
- [📈 Allure Reports](https://mamidisrisaiteja.github.io/ECommercePortal_16Aug01/allure-report/)
- [🔍 GitHub Actions](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/actions)

## Continuous Integration

The framework is ready for CI/CD integration with:
- GitHub Actions
- Jenkins
- Azure DevOps
- GitLab CI

Example GitHub Actions workflow:
```yaml
name: Test Automation
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install
      - name: Run tests
        run: pytest --browser=chromium --headed=false
```

## Best Practices

1. **Page Objects**: Keep page objects focused and maintainable
2. **Step Definitions**: Make steps reusable across scenarios
3. **Test Data**: Externalize test data for easy maintenance
4. **Assertions**: Use clear and meaningful assertions
5. **Logging**: Add appropriate logging for debugging
6. **Screenshots**: Capture evidence for failures

## Troubleshooting

### Common Issues

1. **Browser not found**: Run `playwright install`
2. **Import errors**: Check Python path and virtual environment
3. **Timeout errors**: Increase timeout values in configuration
4. **Test failures**: Check logs and screenshots in reports folder

### Debug Mode

Set environment variable for verbose logging:
```bash
export DEBUG=true
pytest
```

## Contributing

1. Follow the existing code structure
2. Add appropriate tests for new features
3. Update documentation
4. Follow Python PEP 8 style guidelines

## Framework Architecture

This framework leverages the **Playwright MCP Server** for:
- Recording user interactions
- Generating test scripts
- Browser automation
- Element identification
- Cross-browser testing capabilities

The framework is built with modularity and maintainability in mind, following industry best practices for test automation.
