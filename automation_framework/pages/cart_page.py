from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    """Shopping cart page object"""
    
    # Locators
    CART_TITLE = '.title'
    CART_ITEMS = '.cart_item'
    CART_ITEM_NAMES = '.inventory_item_name'
    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'
    REMOVE_BUTTONS = '.cart_button'
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def get_page_url(self) -> str:
        return "/cart.html"
    
    def is_page_loaded(self) -> bool:
        """Check if cart page is loaded"""
        return self.verify_text_present("Your Cart")
    
    def verify_cart_page(self) -> bool:
        """Verify cart page is displayed with 'Your Cart' text"""
        return self.verify_text_present("Your Cart")
    
    def get_cart_items_count(self) -> int:
        """Get the number of items in cart"""
        return len(self.page.locator(self.CART_ITEMS).all())
    
    def get_cart_item_names(self) -> list:
        """Get list of all cart item names"""
        item_names = []
        items = self.page.locator(self.CART_ITEM_NAMES).all()
        for item in items:
            name = item.text_content()
            if name:
                item_names.append(name)
        return item_names
    
    def verify_item_in_cart(self, item_name: str) -> bool:
        """Verify specific item is in cart"""
        cart_items = self.get_cart_item_names()
        return item_name in cart_items
    
    def click_continue_shopping(self) -> None:
        """Click continue shopping button"""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
    
    def click_checkout(self) -> None:
        """Click checkout button"""
        self.click_element(self.CHECKOUT_BUTTON)
    
    def remove_first_item(self) -> None:
        """Remove the first item from cart"""
        first_remove_button = self.page.locator(self.REMOVE_BUTTONS).first
        first_remove_button.click()
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        return self.get_cart_items_count() == 0
