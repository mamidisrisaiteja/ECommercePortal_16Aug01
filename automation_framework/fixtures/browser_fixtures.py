import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright
from typing import Generator
from config.config import Config
from utils.logger import Logger
from utils.helpers import ScreenshotHelper

logger = Logger.get_logger("fixtures")

@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    """Playwright fixture for the session"""
    logger.info("Starting Playwright")
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser_config():
    """Browser configuration fixture"""
    return Config.get_browser_config()

@pytest.fixture(scope="session")
def browser(playwright: Playwright, browser_config) -> Generator[Browser, None, None]:
    """Browser fixture for the session"""
    browser_name = browser_config.get("name", "chromium")
    headless = browser_config.get("headless", False)
    
    logger.info(f"Launching {browser_name} browser (headless: {headless})")
    
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        browser = playwright.chromium.launch(headless=headless)
    
    yield browser
    logger.info("Closing browser")
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser, browser_config) -> Generator[BrowserContext, None, None]:
    """Browser context fixture for each test function"""
    viewport = browser_config.get("viewport", {"width": 1280, "height": 720})
    
    logger.info("Creating new browser context")
    context = browser.new_context(
        viewport=viewport,
        record_video_dir="reports/videos" if Config.load_config().get("record_video", False) else None
    )
    
    yield context
    logger.info("Closing browser context")
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Page fixture for each test function"""
    logger.info("Creating new page")
    page = context.new_page()
    
    # Setup page event listeners
    page.on("console", lambda msg: logger.info(f"Console {msg.type}: {msg.text}"))
    page.on("pageerror", lambda error: logger.error(f"Page error: {error}"))
    
    yield page
    logger.info("Closing page")
    page.close()

@pytest.fixture(scope="function")
def base_url():
    """Base URL fixture"""
    return Config.get_base_url()

@pytest.fixture(scope="function")
def test_data():
    """Test data fixture"""
    return Config.get_test_data()

@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, page: Page):
    """Automatically take screenshot on test failure"""
    yield
    
    if hasattr(request.node, 'rep_setup') and hasattr(request.node, 'rep_call'):
        if request.node.rep_setup.failed or request.node.rep_call.failed:
            screenshot_dir = ScreenshotHelper.create_screenshot_dir()
            test_name = request.node.name
            screenshot_name = ScreenshotHelper.generate_screenshot_name(test_name, "failure")
            screenshot_path = screenshot_dir / screenshot_name
            
            logger.info(f"Test failed, taking screenshot: {screenshot_path}")
            page.screenshot(path=str(screenshot_path))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot on failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)