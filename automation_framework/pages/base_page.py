from abc import ABC, abstractmethod
from typing import Any, Optional
from playwright.sync_api import Page, Locator, expect
import logging

class BasePage(ABC):
    """Base page class for all page objects"""
    
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def get_page_url(self) -> str:
        """Return the URL of the page"""
        pass
    
    @abstractmethod
    def is_page_loaded(self) -> bool:
        """Check if the page is loaded correctly"""
        pass
    
    def navigate_to(self, url: str) -> None:
        """Navigate to a specific URL"""
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)
    
    def wait_for_page_load(self, timeout: int = 30000) -> None:
        """Wait for the page to load completely"""
        self.page.wait_for_load_state("networkidle", timeout=timeout)
    
    def get_page_title(self) -> str:
        """Get the page title"""
        return self.page.title()
    
    def get_current_url(self) -> str:
        """Get the current URL"""
        return self.page.url
    
    def wait_for_element(self, selector: str, timeout: int = 30000) -> None:
        """Wait for an element to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def click_element(self, selector: str) -> None:
        """Click an element"""
        self.logger.info(f"Clicking element: {selector}")
        self.page.click(selector)
    
    def fill_input(self, selector: str, value: str) -> None:
        """Fill an input field"""
        self.logger.info(f"Filling input {selector} with value: {value}")
        self.page.fill(selector, value)
    
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).text_content() or ""
    
    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible"""
        try:
            return self.page.locator(selector).is_visible()
        except Exception:
            return False
    
    def wait_for_text(self, text: str, timeout: int = 30000) -> None:
        """Wait for specific text to appear on the page"""
        self.logger.info(f"Waiting for text: {text}")
        self.page.wait_for_selector(f"text={text}", timeout=timeout)
    
    def verify_text_present(self, text: str) -> bool:
        """Verify if specific text is present on the page"""
        try:
            expect(self.page.locator(f"text={text}")).to_be_visible()
            return True
        except AssertionError:
            self.logger.error(f"Text '{text}' not found on page")
            return False
    
    def take_screenshot(self, name: str) -> str:
        """Take a screenshot and return the path"""
        screenshot_path = f"reports/screenshots/{name}.png"
        self.page.screenshot(path=screenshot_path)
        self.logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path