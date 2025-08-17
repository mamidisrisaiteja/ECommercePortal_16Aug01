# Development Automation
.PHONY: help install test test-auth test-smoke test-regression clean lint format report

# Default target
help:
	@echo "ECommerce Portal Test Automation Framework"
	@echo "=========================================="
	@echo "Available targets:"
	@echo "  install       - Install all dependencies"
	@echo "  test          - Run all tests"
	@echo "  test-auth     - Run authentication tests"
	@echo "  test-smoke    - Run smoke tests"
	@echo "  test-regression - Run regression tests"
	@echo "  test-headed   - Run tests in headed mode"
	@echo "  clean         - Clean reports and cache"
	@echo "  lint          - Run code linting"
	@echo "  format        - Format code"
	@echo "  report        - Generate and serve Allure report"
	@echo "  setup-dev     - Setup development environment"

# Installation
install:
	@echo "Installing dependencies..."
	cd automation_framework && pip install -r requirements.txt
	@echo "Installing Playwright browsers..."
	cd automation_framework && playwright install
	@echo "Installation complete!"

# Test execution
test:
	@echo "Running all tests..."
	cd automation_framework && pytest -m auth -v --alluredir=reports/allure-results

test-auth:
	@echo "Running authentication tests..."
	cd automation_framework && pytest -m auth -v --alluredir=reports/allure-results

test-smoke:
	@echo "Running smoke tests..."
	cd automation_framework && pytest -m "auth and smoke" -v --alluredir=reports/allure-results

test-regression:
	@echo "Running regression tests..."
	cd automation_framework && pytest -m "auth and regression" -v --alluredir=reports/allure-results

test-headed:
	@echo "Running tests in headed mode..."
	cd automation_framework && pytest -m auth -v --headed --alluredir=reports/allure-results

# Multi-browser testing
test-chromium:
	@echo "Running tests on Chromium..."
	cd automation_framework && pytest -m auth -v --browser=chromium --alluredir=reports/allure-results

test-firefox:
	@echo "Running tests on Firefox..."
	cd automation_framework && pytest -m auth -v --browser=firefox --alluredir=reports/allure-results

test-webkit:
	@echo "Running tests on WebKit..."
	cd automation_framework && pytest -m auth -v --browser=webkit --alluredir=reports/allure-results

# Development tools
setup-dev:
	@echo "Setting up development environment..."
	cd automation_framework && pip install -r requirements.txt
	cd automation_framework && playwright install
	cd automation_framework && pip install black flake8 mypy
	@echo "Development environment ready!"

lint:
	@echo "Running code linting..."
	cd automation_framework && flake8 .
	cd automation_framework && mypy . --ignore-missing-imports

format:
	@echo "Formatting code..."
	cd automation_framework && black .

# Reporting
report:
	@echo "Generating Allure report..."
	cd automation_framework && allure generate reports/allure-results --clean -o reports/allure-report
	@echo "Serving Allure report..."
	cd automation_framework && allure serve reports/allure-results

# Cleanup
clean:
	@echo "Cleaning reports and cache..."
	cd automation_framework && rm -rf reports/screenshots/*
	cd automation_framework && rm -rf reports/videos/*
	cd automation_framework && rm -rf reports/logs/*
	cd automation_framework && rm -rf reports/allure-results/*
	cd automation_framework && rm -rf reports/allure-report/*
	cd automation_framework && rm -rf __pycache__
	cd automation_framework && rm -rf .pytest_cache
	cd automation_framework && find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Cleanup complete!"

# CI/CD helpers
ci-install:
	@echo "Installing for CI environment..."
	cd automation_framework && pip install -r requirements.txt
	cd automation_framework && playwright install --with-deps

ci-test:
	@echo "Running CI tests..."
	cd automation_framework && pytest -m auth -v --browser=chromium --headed=false --alluredir=reports/allure-results --html=reports/ci_report.html --self-contained-html

# Docker support (future enhancement)
docker-build:
	@echo "Building Docker image..."
	docker build -t ecommerce-portal-tests .

docker-run:
	@echo "Running tests in Docker..."
	docker run --rm -v $(PWD)/automation_framework/reports:/app/reports ecommerce-portal-tests

# Documentation
docs:
	@echo "Generating documentation..."
	mkdir -p docs
	cp README.md docs/
	@echo "Documentation ready in docs/ directory"