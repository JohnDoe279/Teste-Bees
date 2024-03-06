from selenium.webdriver.common.by import By
from features.pageobjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "user_email": (By.ID, "user_email"),
        "user_password": (By.ID, "user_password"),
        "sign_up_user_password_confirmation": (By.ID, "user_password_confirmation"),
        "sign_up_submit_btn": (By.XPATH, "//*[@id='new_user']/div[2]/input"),
        "signed_up_success_msg": (By.XPATH, "//html/body/div/p[(text()='Welcome! You have signed up successfully.')]"),
        "login_sign_up_btn": (By.XPATH, "//html/body/div/a[(text()='Sign up')]"),
        "signed_is_success_msg": (By.XPATH, "//html/body/div/p[(text()='Signed in successfully.')]")

    }

    def enter_email(self, email):
        self.enter_text(self.locators["user_email"], email)

    def enter_password(self, password):
        self.enter_text(self.locators["user_password"], password)

    def confirm_password(self, password):
        self.enter_text(self.locators["sign_up_user_password_confirmation"], password)

    def click_sign_up(self):
        self.click_element(self.locators["login_sign_up_btn"])
        self.wait_for_element_visibility(self.locators["sign_up_user_password_confirmation"])

    def submit_form(self):
        self.click_element(self.locators["sign_up_submit_btn"])

    def is_welcome_message_displayed(self):
        try:
            self.wait_for_element_visibility(self.locators["signed_up_success_msg"], timeout=5)
            return True
        except:
            return False

    def get_page_title(self):
        return self.driver.title

    def is_sign_in_message_displayed(self):
        try:
            self.wait_for_element_visibility(self.locators["signed_is_success_msg"], timeout=5)
            return True
        except:
            return False

    def sign_in(self, email, password):
        self.login(email, password)



