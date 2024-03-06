from behave import *
from Utilities import configReader


@given(u'that I am in home page')
def step_impl(context):
    context.base_page.login(configReader.readConfig("user info", "email"),
                            configReader.readConfig("user info", "password"))


@when(u'I click on "{page}"')
def step_impl(context, page):
    context.home_page.access_page(page)


@then(u'"{page}" page is displayed')
def step_impl(context, page):
    assert context.home_page.is_page_displayed(page)
