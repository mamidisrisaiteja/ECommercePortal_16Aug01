# ECommerce Portal Test Automation Framework

## Overview
This is a comprehensive test automation framework for the ECommerce Portal using Python, Playwright, Pytest, and BDD.

## Framework Structure
```
automation_framework/
├── config/
│   ├── config.py          # Configuration management
│   └── default.yaml       # Default configuration settings
├── pages/
│   ├── base_page.py       # Base page object class
│   ├── login_page.py      # Login page object
│   └── products_page.py   # Products page object
├── tests/
│   ├── features/
│   │   └── authentication.feature  # BDD feature files
│   └── step_definitions/
│       └── auth_steps.py      # Step definitions
├── fixtures/
│   └── browser_fixtures.py # Pytest fixtures
├── utils/
│   ├── logger.py          # Logging utility
│   └── helpers.py         # Helper utilities
├── requirements.txt       # Python dependencies
├── pytest.ini           # Pytest configuration
└── conftest.py          # Global pytest configuration
```

## Test Scenarios

### Authentication Module
- **TC_AUTH_01**: Login with valid credentials
  - Tags: `@auth @smoke`
  - Validates successful login with standard_user/secret_sauce
  - Verifies redirect to Products page

- **TC_AUTH_02**: Login with invalid credentials
  - Tags: `@auth @regression`
  - Validates error handling with invalid credentials
  - Verifies user remains on login page

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01.git
cd ECommercePortal_16Aug01/automation_framework

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Running Tests

```bash
# Run all authentication tests
pytest -m auth

# Run smoke tests only
pytest -m "auth and smoke"

# Run regression tests only
pytest -m "auth and regression"

# Run with specific browser
pytest -m auth --browser=firefox

# Run in headed mode (visible browser)
pytest -m auth --headed

# Generate Allure report
pytest -m auth --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Configuration

### Browser Configuration
Edit `config/default.yaml` to modify:
- Browser type (chromium, firefox, webkit)
- Headless mode
- Viewport size
- Timeouts

### Environment Variables
- `BASE_URL`: Override base URL
- `BROWSER_NAME`: Override browser (chromium, firefox, webkit)
- `HEADLESS`: Set to 'true' for headless mode
- `TEST_ENV`: Environment (default, staging, production)

## CI/CD Pipeline

The framework includes comprehensive GitHub Actions workflows:

### Smoke Tests
- Triggers on every push to main and pull requests
- Runs critical test scenarios (@smoke tag)
- Fast feedback for basic functionality

### Regression Tests
- Comprehensive test suite
- Multi-browser testing (Chromium, Firefox, WebKit)
- Multi-Python version support (3.9, 3.10, 3.11)
- Scheduled daily runs

### Release Pipeline
- Validates all tests before release
- Generates documentation
- Creates release artifacts

## Reporting

### Built-in Reports
- **HTML Report**: Generated with pytest-html
- **Allure Report**: Interactive test reporting
- **JUnit XML**: For CI/CD integration
- **Screenshots**: Automatic capture on failures
- **Logs**: Detailed execution logs

### Report Locations
- `reports/screenshots/`: Test failure screenshots
- `reports/logs/`: Execution logs
- `reports/allure-results/`: Allure test results
- `reports/allure-report/`: Generated Allure HTML report

## Page Object Model

The framework implements the Page Object Model pattern:

### BasePage
- Abstract base class for all page objects
- Common functionality (navigation, element interaction)
- Screenshot capture
- Logging integration

### LoginPage
- Username/password input methods
- Login button interaction
- Error message validation
- Page state verification

### ProductsPage
- Product listing verification
- Cart interaction
- Navigation verification

## BDD Implementation

### Feature Files
- Written in Gherkin syntax
- Located in `tests/features/`
- Tagged for test organization

### Step Definitions
- Python implementations of Gherkin steps
- Located in `tests/step_definitions/`
- Reusable across scenarios

## Troubleshooting

### Common Issues

1. **Browser Installation**
   ```bash
   playwright install
   ```

2. **Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Path Issues**
   - Ensure you're in the `automation_framework` directory
   - Check relative paths in configuration

4. **Permissions**
   - On Windows, run VS Code as administrator if needed
   - Check file/directory permissions

### Debug Mode
```bash
# Run with debug logging
pytest -m auth -s -v --log-cli-level=DEBUG

# Run with Playwright debug
PWDEBUG=1 pytest -m auth --headed
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review existing GitHub issues
3. Create a new issue with detailed information

---

**Framework Version**: 1.0.0  
**Last Updated**: January 2025  
**Maintainer**: ECommerce Portal QA Team