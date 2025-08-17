# Makefile for ECommercePortal Test Automation Framework

.PHONY: help install test test-smoke test-regression test-auth clean setup lint format reports

# Default target
help:
	@echo "🚀 ECommercePortal Test Automation Framework"
	@echo ""
	@echo "Available commands:"
	@echo "  setup           - Install dependencies and setup environment"
	@echo "  install         - Install Python dependencies"
	@echo "  test            - Run all tests"
	@echo "  test-smoke      - Run smoke tests (TC_AUTH_01)"
	@echo "  test-regression - Run regression tests (TC_AUTH_02)"
	@echo "  test-auth       - Run all authentication tests"
	@echo "  test-headed     - Run tests with visible browser"
	@echo "  lint            - Run code linting"
	@echo "  format          - Format code"
	@echo "  clean           - Clean reports and cache"
	@echo "  reports         - Generate and serve Allure reports"

# Setup environment
setup: install
	@echo "🎭 Installing Playwright browsers..."
	playwright install
	@echo "✅ Setup completed!"

# Install dependencies
install:
	@echo "📦 Installing Python dependencies..."
	pip install -r requirements.txt

# Run all tests
test:
	@echo "🧪 Running all tests..."
	pytest tests/ \
		--browser=chromium \
		--headed=false \
		--html=reports/report.html \
		--self-contained-html \
		--alluredir=reports/allure-results \
		-v

# Run smoke tests
test-smoke:
	@echo "🚀 Running smoke tests (TC_AUTH_01)..."
	pytest tests/ \
		--browser=chromium \
		--headed=false \
		-m "smoke" \
		--html=reports/smoke-report.html \
		--self-contained-html \
		-v

# Run regression tests
test-regression:
	@echo "🔄 Running regression tests (TC_AUTH_02)..."
	pytest tests/ \
		--browser=chromium \
		--headed=false \
		-m "regression" \
		--html=reports/regression-report.html \
		--self-contained-html \
		-v

# Run authentication tests
test-auth:
	@echo "🔐 Running authentication tests..."
	pytest tests/ \
		--browser=chromium \
		--headed=false \
		-m "auth" \
		--html=reports/auth-report.html \
		--self-contained-html \
		--alluredir=reports/allure-results \
		-v

# Run tests with visible browser
test-headed:
	@echo "👀 Running tests with visible browser..."
	pytest tests/ \
		--browser=chromium \
		--headed=true \
		-m "auth" \
		--html=reports/headed-report.html \
		--self-contained-html \
		-v

# Run tests with Firefox
test-firefox:
	@echo "🦊 Running tests with Firefox..."
	pytest tests/ \
		--browser=firefox \
		--headed=false \
		-m "auth" \
		--html=reports/firefox-report.html \
		--self-contained-html \
		-v

# Run tests with WebKit
test-webkit:
	@echo "🌐 Running tests with WebKit..."
	pytest tests/ \
		--browser=webkit \
		--headed=false \
		-m "auth" \
		--html=reports/webkit-report.html \
		--self-contained-html \
		-v

# Run parallel tests
test-parallel:
	@echo "⚡ Running tests in parallel..."
	pytest tests/ \
		--browser=chromium \
		--headed=false \
		-n auto \
		--html=reports/parallel-report.html \
		--self-contained-html \
		-v

# Code linting
lint:
	@echo "🔍 Running code linting..."
	flake8 pages/ utils/ fixtures/ tests/ --max-line-length=100
	pylint pages/ utils/ fixtures/ tests/ --disable=C0114,C0115,C0116

# Code formatting
format:
	@echo "✨ Formatting code..."
	black pages/ utils/ fixtures/ tests/ --line-length=100
	isort pages/ utils/ fixtures/ tests/

# Clean reports and cache
clean:
	@echo "🧹 Cleaning reports and cache..."
	rm -rf reports/
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +
	@echo "✅ Cleanup completed!"

# Generate and serve Allure reports
reports:
	@echo "📊 Generating Allure reports..."
	allure generate reports/allure-results --clean -o reports/allure-report
	@echo "🌐 Serving Allure reports..."
	allure serve reports/allure-results

# Create reports directory
reports-dir:
	@mkdir -p reports/screenshots
	@mkdir -p reports/videos
	@mkdir -p reports/logs
	@mkdir -p reports/allure-results

# Development setup
dev-setup: setup reports-dir
	@echo "🛠️  Installing development dependencies..."
	pip install flake8 pylint black isort
	@echo "✅ Development environment ready!"

# CI/CD simulation
ci-test: clean install
	@echo "🤖 Running CI/CD simulation..."
	playwright install chromium
	pytest tests/ \
		--browser=chromium \
		--headed=false \
		--html=reports/ci-report.html \
		--self-contained-html \
		--alluredir=reports/allure-results \
		--junitxml=reports/junit.xml \
		-v

# Test specific test case
test-tc-auth-01:
	@echo "🧪 Running TC_AUTH_01..."
	pytest tests/ -k "TC_AUTH_01" \
		--browser=chromium \
		--headed=false \
		--html=reports/tc-auth-01-report.html \
		--self-contained-html \
		-v

test-tc-auth-02:
	@echo "🧪 Running TC_AUTH_02..."
	pytest tests/ -k "TC_AUTH_02" \
		--browser=chromium \
		--headed=false \
		--html=reports/tc-auth-02-report.html \
		--self-contained-html \
		-v

# Environment info
info:
	@echo "ℹ️  Environment Information:"
	@echo "Python version: $(shell python --version)"
	@echo "Pip version: $(shell pip --version)"
	@echo "Pytest version: $(shell pytest --version)"
	@echo "Current directory: $(shell pwd)"
	@echo "Repository: https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01"
