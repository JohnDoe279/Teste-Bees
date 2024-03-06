import allure
import json
from selenium import webdriver
from Utilities import configReader
from features.pageobjects.BasePage import BasePage
from features.pageobjects.DepositsPage import DepositsPage
from features.pageobjects.HomePage import HomePage
from features.pageobjects.ItemsPage import ItemsPage
from features.pageobjects.LoginPage import LoginPage


def before_tag(context, tag):
    if (tag == "api" or tag == "people_api" or tag == "films_api" or tag == "planets_api" or tag == "species_api" or
            tag == "starships_api" or tag == "vehicles_api"):
        return
    browser_name = configReader.readConfig("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(configReader.readConfig("basic info", "url"))
    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)
    context.base_page = BasePage(context.driver)
    context.deposits_page = DepositsPage(context.driver)
    context.items_page = ItemsPage(context.driver)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_step(context, step):
    if hasattr(context, 'driver') and context.driver is not None:
        if step.status == 'failed':
            allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
