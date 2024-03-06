import time

from behave import *
from Utilities import configReader


@given(u'that I am in deposits page')
def step_impl(context):
    context.base_page.login(configReader.readConfig("user info", "email"),
                            configReader.readConfig("user info", "password"))
    context.home_page.access_page("Deposits")


@when(u'I click on New Deposit')
def step_impl(context):
    context.deposits_page.click_new_deposit()


@when(u'fill new deposit Name as "{name}"')
def step_impl(context, name):
    context.deposits_page.type_deposit_name(name)


@when(u'fill new deposit Address as "{address}"')
def step_impl(context, address):
    context.deposits_page.type_address(address)


@when(u'fill new deposit City as "{city}"')
def step_impl(context, city):
    context.deposits_page.type_city(city)


@when(u'fill new deposit State as "{state}"')
def step_impl(context, state):
    context.deposits_page.type_state(state)


@when(u'fill new deposit Zipcode as "{zipcode}"')
def step_impl(context, zipcode):
    context.deposits_page.type_zipcode(zipcode)


@when(u'I click on  Create Deposit')
def step_impl(context):
    context.deposits_page.create_new_deposit()
    assert context.deposits_page.is_deposit_created_msg() == "Deposit was successfully created."


@then(u'I see the deposit in deposits list "{name}""{address}""{city}""{state}""{zipcode}"')
def step_impl(context, name, address, city, state, zipcode):
    context.deposits_page.back_to_deposit()
    assert context.deposits_page.is_deposit_created(name)
    assert context.deposits_page.is_deposit_created(address)
    assert context.deposits_page.is_deposit_created(city)
    assert context.deposits_page.is_deposit_created(state)
    assert context.deposits_page.is_deposit_created(zipcode)


@when(u'I click on "{old_name}" to show the deposit data')
def step_impl(context, old_name):
    context.deposits_page.click_show_deposit_for_item(old_name)


@when(u'I click to edit the deposit')
def step_impl(context):
    context.deposits_page.edit_deposit()


@when(u'I click on Update Deposit')
def step_impl(context):
    context.deposits_page.update_deposit()
    assert context.deposits_page.is_deposit_updated() == "Deposit was successfully updated."


@when(u'I click to destroy the deposit')
def step_impl(context):
    context.deposits_page.destroy_deposit()


@then(u'I do not see "{name}" deposit in deposits list')
def step_impl(context, name):
    context.deposits_page.is_deposit_destroyed(name)
