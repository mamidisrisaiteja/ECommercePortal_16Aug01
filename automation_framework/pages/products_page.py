from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """Products/Inventory page object"""
    
    # Locators
    PRODUCTS_TITLE = '.title'
    INVENTORY_CONTAINER = '.inventory_container'
    INVENTORY_ITEMS = '.inventory_item'
    ADD_TO_CART_BUTTONS = '.btn_inventory'
    SHOPPING_CART_LINK = '.shopping_cart_link'
    SORT_DROPDOWN = '[data-test="product_sort_container"]'
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def get_page_url(self) -> str:
        return "/inventory.html"
    
    def is_page_loaded(self) -> bool:
        """Check if products page is loaded"""
        return self.is_element_visible(self.PRODUCTS_TITLE) and self.verify_text_present("Products")
    
    def verify_products_page(self) -> bool:
        """Verify products page is displayed with 'Products' text"""
        return self.verify_text_present("Products")
    
    def verify_add_to_cart_present(self) -> bool:
        """Verify 'Add to cart' text is present"""
        return self.verify_text_present("Add to cart")
    
    def get_products_count(self) -> int:
        """Get the number of products displayed"""
        return len(self.page.locator(self.INVENTORY_ITEMS).all())
    
    def add_first_product_to_cart(self) -> None:
        """Add the first product to cart"""
        first_add_button = self.page.locator(self.ADD_TO_CART_BUTTONS).first
        first_add_button.click()
    
    def click_shopping_cart(self) -> None:
        """Click the shopping cart icon"""
        self.click_element(self.SHOPPING_CART_LINK)
    
    def sort_products_by_name_a_to_z(self) -> None:
        """Sort products by name A to Z"""
        self.page.select_option(self.SORT_DROPDOWN, "az")
    
    def get_product_names(self) -> list:
        """Get list of all product names"""
        product_names = []
        products = self.page.locator(self.INVENTORY_ITEMS).all()
        for product in products:
            name = product.locator('.inventory_item_name').text_content()
            if name:
                product_names.append(name)
        return product_names
    
    def verify_products_sorted_a_to_z(self) -> bool:
        """Verify products are sorted A to Z"""
        product_names = self.get_product_names()
        sorted_names = sorted(product_names)
        return product_names == sorted_names