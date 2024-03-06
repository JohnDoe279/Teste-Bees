from selenium.webdriver.common.by import By
from features.pageobjects.BasePage import BasePage


class DepositsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "new_deposit_btn": (By.XPATH, "//html/body/div/a[(text()='New deposit')]"),
        "deposit_name": (By.ID, "deposit_name"),
        "deposit_address": (By.ID, "deposit_address"),
        "deposit_city": (By.ID, "deposit_city"),
        "deposit_state": (By.ID, "deposit_state"),
        "deposit_zipcode": (By.ID, "deposit_zipcode"),
        "create_deposit_btn": (By.XPATH, "//*[@id='new_deposit']/div[2]/input"),
        "back_to_deposits_btn": (By.XPATH, "//a[text()='Back to deposits']"),
        "deposits_table": (By.XPATH, "//*[@id='deposits']/table/tbody"),
        "edit_this_deposit_btn": (By.XPATH, "//html/body/div/div[2]/a[(text()='Edit this deposit')]"),
        "update_deposit_btn": (By.XPATH, "//input[contains(@value,'Update Deposit')]"),
        "destroy_this_deposit_btn": (By.XPATH, "//button[text()='Destroy this deposit']"),
        "new_deposit_creation_success_msg": (By.XPATH, "//p[normalize-space()='Deposit was successfully created.']"),
        "update_deposit_success_msg": (By.XPATH, "//p[normalize-space()='Deposit was successfully updated.']")

    }

    def click_new_deposit(self):
        self.click_element(self.locators["new_deposit_btn"])

    def type_deposit_name(self, name):
        self.enter_text(self.locators["deposit_name"], name)

    def type_address(self, address):
        self.enter_text(self.locators["deposit_address"], address)

    def type_city(self, city):
        self.enter_text(self.locators["deposit_city"], city)

    def type_state(self, state):
        self.enter_text(self.locators["deposit_state"], state)

    def type_zipcode(self, zipcode):
        self.enter_text(self.locators["deposit_zipcode"], zipcode)

    def create_new_deposit(self):
        self.click_element(self.locators["create_deposit_btn"])

    def back_to_deposit(self):
        self.click_element(self.locators["back_to_deposits_btn"])

    def is_deposit_created(self, deposit_data):
        return self.is_item_present_in_table(self.locators["deposits_table"], deposit_data)

    def is_deposit_destroyed(self, deposit_data):
        return self.is_item_not_present_in_table(self.locators["deposits_table"], deposit_data)

    def click_show_deposit_for_item(self, deposit_data):
        # get table data
        rows_data = self.get_table_rows_data(self.locators["deposits_table"])

        # search for an item in the lines
        for row_data in rows_data:
            if deposit_data in row_data:
                # If it finds the item clicks on 'Show this deposit'
                self.finds_item_and_click(
                    self.locators["deposits_table"], rows_data.index(row_data))
                return

        # If item is not found, raise an error
        raise ValueError(f"Item '{deposit_data}' not found in the table.")

    def edit_deposit(self):
        self.click_element(self.locators["edit_this_deposit_btn"])

    def update_deposit(self):
        self.click_element(self.locators["update_deposit_btn"])

    def destroy_deposit(self):
        self.click_element(self.locators["destroy_this_deposit_btn"])

    def is_deposit_created_msg(self):
        return self.get_element_text(self.locators["new_deposit_creation_success_msg"])

    def is_deposit_updated(self):
        return self.get_element_text(self.locators["update_deposit_success_msg"])


