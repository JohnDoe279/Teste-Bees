from selenium.webdriver.common.by import By
from features.pageobjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "deposit_link": (By.XPATH, "//a[normalize-space()='Deposits']"),
        "items_link": (By.XPATH, "//a[normalize-space()='Items']"),
        "inventory_link": (By.XPATH, "//a[normalize-space()='Inventory']"),
        "deposit_header": (By.XPATH, "//html/body/div/h1[(text()='Deposits')]"),
        "items_header": (By.XPATH, "//html/body/div/h1[(text()='Items')]"),
        "inventory_header": (By.XPATH, "//html/body/div/h1[(text()='Inventories')]"),
    }

    def access_page(self, page):
        if page.__eq__("Deposits"):
            self.click_element(self.locators["deposit_link"])
        if page.__eq__("Items"):
            self.click_element(self.locators["items_link"])
        if page.__eq__("Inventory"):
            self.click_element(self.locators["inventory_link"])

    def is_page_displayed(self, page):
        try:
            if page.__eq__("Deposits"):
                self.wait_for_element_visibility(self.locators["deposit_header"], timeout=5)
                return True
            if page.__eq__("Items"):
                self.wait_for_element_visibility(self.locators["items_header"], timeout=5)
                return True
            if page.__eq__("Inventory"):
                self.wait_for_element_visibility(self.locators["inventory_header"], timeout=5)
                return True
        except:
            return False
