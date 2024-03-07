from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Utilities import configReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "user_email": (By.ID, "user_email"),
        "user_password": (By.ID, "user_password"),
        "sign_up_submit_btn": (By.XPATH, "//*[@id='new_user']/div[2]/input")
    }

    def get_page_title(self) -> str:
        return self.driver.title

    def enter_text(self, locator, text):
        self.wait_for_element_visibility(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_page_to_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def login(self, email, password):
        self.enter_text(self.locators["user_email"], email)
        self.enter_text(self.locators["user_password"], password)
        self.click_element(self.locators["sign_up_submit_btn"])
        self.wait_for_page_to_load()

    def get_element_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            print("Element not found or not visible within 10 seconds.")
            return None

    def get_table_rows_data(self, table_locator):
        table = self.wait_for_element_visibility(table_locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        rows_data = []

        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = [column.text for column in columns]
            rows_data.append(row_data)

        return rows_data

    def is_item_present_in_table(self, table_locator, item):
        self.wait_for_element_visibility(table_locator)
        rows_data = self.get_table_rows_data(table_locator)

        for row_data in rows_data:
            if item in row_data:
                return True

        return False

    def is_item_not_present_in_table(self, table_locator, item):
        self.wait_for_element_visibility(table_locator)
        rows_data = self.get_table_rows_data(table_locator)

        for row_data in rows_data:
            if item in row_data:
                return False

        return True

    def finds_item_and_click(self, table_locator, row_index):
        table = self.wait_for_element_visibility(table_locator)
        row = table.find_elements(By.TAG_NAME, "tr")[row_index]
        columns = row.find_elements(By.TAG_NAME, "td")

        for column in columns:
            if column.text.strip() in ["Show this deposit", "Show this item"]:
                column.click()
                return  

        raise NoSuchElementException("Item not found in any column")


