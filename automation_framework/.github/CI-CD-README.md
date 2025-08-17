# CI/CD Configuration for ECommercePortal Test Framework

## Environment Variables
The following environment variables can be configured in GitHub repository settings:

### Required Secrets:
- `SLACK_WEBHOOK_URL`: Slack webhook URL for notifications (optional)

### Environment Variables:
- `BASE_URL`: Base URL for testing (default: https://www.saucedemo.com)
- `BROWSER_NAME`: Default browser (chromium, firefox, webkit)
- `HEADLESS`: Run tests in headless mode (true/false)
- `TEST_ENV`: Test environment (staging, production)

## Pipeline Triggers

### 1. Regression Test Pipeline (`regression-tests.yml`)
**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` branch
- Scheduled daily at 2 AM UTC
- Manual dispatch with configurable parameters

**Features:**
- Multi-browser testing (Chromium, Firefox, WebKit)
- Multi-Python version testing (3.9, 3.10, 3.11)
- Parallel execution with matrix strategy
- Comprehensive reporting (HTML, Allure, JUnit)
- Security scanning
- Slack notifications
- GitHub Pages deployment for Allure reports

### 2. Smoke Test Pipeline (`smoke-tests.yml`)
**Triggers:**
- Push to `main` branch
- Pull requests to `main` branch
- Manual dispatch

**Features:**
- Quick validation with TC_AUTH_01
- Single browser (Chromium) for speed
- Fast feedback loop

### 3. Release Pipeline (`release.yml`)
**Triggers:**
- Git tags matching `v*.*.*` pattern
- Manual dispatch with version input

**Features:**
- Full test suite execution
- Automated release creation
- Framework archive generation
- Release notes generation

## Test Execution Matrix

| Pipeline | Browsers | Python Versions | Test Tags | Duration |
|----------|----------|-----------------|-----------|----------|
| Smoke | Chromium | 3.11 | smoke | ~2 min |
| Regression | Chromium, Firefox, WebKit | 3.9, 3.10, 3.11 | auth, regression | ~15 min |
| Release | All | 3.11 | all | ~5 min |

## Artifacts Generated

### Test Reports:
- HTML reports with screenshots
- Allure reports (deployed to GitHub Pages)
- JUnit XML for test integration
- Test execution logs

### Security Scan:
- Code quality analysis
- Security vulnerability detection
- Dependency checking

## Notifications

### Slack Integration:
- Success notifications with test summary
- Failure notifications with debug links
- Scheduled test results

### GitHub:
- Status checks on pull requests
- Test summary in workflow runs
- Automatic issue creation on failures (future enhancement)

## Manual Workflow Dispatch

All pipelines support manual execution with parameters:

### Regression Tests:
- **Test Tags**: auth, smoke, regression, all
- **Browser**: chromium, firefox, webkit
- **Environment**: staging, production

### Example Usage:
```bash
# Trigger via GitHub CLI
gh workflow run regression-tests.yml \
  -f test_tags=auth \
  -f browser=chromium \
  -f environment=staging
```

## Monitoring and Reporting

### GitHub Pages Integration:
- Allure reports automatically deployed
- Historical test results tracking
- Trend analysis and metrics

### Status Badges:
Add to README.md:
```markdown
![Regression Tests](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/workflows/Regression%20Test%20Pipeline/badge.svg)
![Smoke Tests](https://github.com/mamidisrisaiteja/ECommercePortal_16Aug01/workflows/Smoke%20Tests/badge.svg)
```

## Best Practices Implemented

1. **Fail-Fast Strategy**: Smoke tests provide quick feedback
2. **Matrix Testing**: Multiple browsers and Python versions
3. **Caching**: Dependencies cached for faster execution
4. **Parallel Execution**: Tests run concurrently when possible
5. **Comprehensive Reporting**: Multiple report formats
6. **Security First**: Automated security scanning
7. **Notification System**: Real-time status updates
8. **Version Control**: Tagged releases with automated deployment

## Future Enhancements

1. **Cross-Platform Testing**: Windows, macOS, Linux
2. **Performance Testing**: Load and stress test integration
3. **Visual Regression**: Screenshot comparison
4. **API Testing**: Backend service validation
5. **Database Testing**: Data validation
6. **Mobile Testing**: Responsive design validation
