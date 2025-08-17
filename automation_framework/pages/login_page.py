from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Login page object"""
    
    # Locators
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'
    LOGIN_LOGO = '.login_logo'
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def get_page_url(self) -> str:
        return "/"
    
    def is_page_loaded(self) -> bool:
        """Check if login page is loaded"""
        return self.is_element_visible(self.LOGIN_LOGO) and self.is_element_visible(self.LOGIN_BUTTON)
    
    def enter_username(self, username: str) -> None:
        """Enter username in the username field"""
        self.fill_input(self.USERNAME_INPUT, username)
    
    def enter_password(self, password: str) -> None:
        """Enter password in the password field"""
        self.fill_input(self.PASSWORD_INPUT, password)
    
    def click_login_button(self) -> None:
        """Click the login button"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username: str, password: str) -> None:
        """Perform login with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self) -> str:
        """Get the error message text"""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_login_button_visible(self) -> bool:
        """Check if login button is visible"""
        return self.is_element_visible(self.LOGIN_BUTTON)
    
    def verify_login_page_displayed(self) -> bool:
        """Verify login page is displayed"""
        return self.is_page_loaded()
    
    def verify_error_message(self, expected_message: str) -> bool:
        """Verify specific error message is displayed"""
        actual_message = self.get_error_message()
        return expected_message in actual_message