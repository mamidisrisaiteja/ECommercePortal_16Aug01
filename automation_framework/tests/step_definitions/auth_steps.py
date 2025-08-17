import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.logger import Logger

# Load scenarios from authentication feature file only
scenarios("../features/authentication.feature")

logger = Logger.get_logger("steps")

# Page objects fixtures
@pytest.fixture
def login_page(page: Page, base_url: str):
    """Login page fixture"""
    login_page = LoginPage(page)
    page.goto(base_url)
    return login_page

# Step definitions for Authentication Module only (TC_AUTH_01 and TC_AUTH_02)
@given("user is on Login Page")
def user_is_on_login_page(login_page: LoginPage):
    """Navigate to login page"""
    logger.info("User is on Login Page")
    assert login_page.is_page_loaded(), "Login page should be loaded"

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(login_page: LoginPage, username: str, password: str):
    """Enter username and password"""
    logger.info(f"Entering credentials: {username}")
    login_page.enter_username(username)
    login_page.enter_password(password)

@when("click Login Button")
def click_login_button(login_page: LoginPage):
    """Click the login button"""
    logger.info("Clicking Login Button")
    login_page.click_login_button()

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text(page: Page, text: str):
    """Verify specific text is present on the page"""
    logger.info(f"Verifying page has text: {text}")
    expect(page.locator(f"text={text}")).to_be_visible()

@then("Login Button should be still displayed")
def login_button_still_displayed(login_page: LoginPage):
    """Verify login button is still displayed"""
    logger.info("Verifying Login Button is still displayed")
    assert login_page.is_login_button_visible(), "Login button should still be visible"