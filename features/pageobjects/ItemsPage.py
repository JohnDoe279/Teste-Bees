from selenium.webdriver.common.by import By
from features.pageobjects.BasePage import BasePage


class ItemsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "new_item_btn": (By.XPATH, "//a[normalize-space()='New item']"),
        "item_name": (By.ID, "item_name"),
        "item_height": (By.ID, "item_height"),
        "item_width": (By.ID, "item_width"),
        "item_weight": (By.ID, "item_weight"),
        "create_item_btn": (By.XPATH, "//input[@value='Create Item']"),
        "back_to_items_btn": (By.XPATH, "//a[normalize-space()='Back to items']"),
        "edit_this_item_btn": (By.XPATH, "//a[normalize-space()='Edit this item']"),
        "update_item_btn": (By.XPATH, "//input[@value='Update Item']"),
        "items_table": (By.XPATH, "//*[@id='items']/table/tbody"),
        "new_item_creation_success_msg": (By.XPATH, "//p[normalize-space()='Item was successfully created.']"),
        "destroy_this_item_btn": (By.XPATH, "")
    }

    def click_new_item(self):
        self.click_element(self.locators["new_item_btn"])

    def type_item_name(self, name):
        self.enter_text(self.locators["item_name"], name)

    def type_item_height(self, height):
        self.enter_text(self.locators["item_height"], height)

    def type_item_width(self, width):
        self.enter_text(self.locators["item_width"], width)

    def type_item_weight(self, weight):
        self.enter_text(self.locators["item_weight"], weight)

    def create_new_item(self):
        self.click_element(self.locators["create_item_btn"])

    def is_item_created_msg(self):
        return self.get_element_text(self.locators["new_item_creation_success_msg"])

    def back_to_items(self):
        self.click_element(self.locators["back_to_items_btn"])

    def is_item_created(self, item_data):
        return self.is_item_present_in_table(self.locators["items_table"], item_data)

    def is_item_destroyed(self, item_data):
        return self.is_item_not_present_in_table(self.locators["items_table"], item_data)

    def click_show_item_for_item(self, item_data):
        # get table data
        rows_data = self.get_table_rows_data(self.locators["deposits_table"])

        # search for an item in the lines
        for row_data in rows_data:
            if item_data in row_data:
                # If it finds the item clicks on 'Show this item'
                self.finds_item_and_click(
                    self.locators["deposits_table"], rows_data.index(row_data))
                return

        # If item is not found, raise an error
        raise ValueError(f"Item '{item_data}' not found in the table.")

    def edit_item(self):
        self.click_element(self.locators["edit_this_item_btn"])

    def destroy_item(self):
        self.click_element(self.locators["destroy_this_item_btn"])
