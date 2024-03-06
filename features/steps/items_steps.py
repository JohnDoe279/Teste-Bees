from behave import *
from Utilities import configReader


@given(u'that I am in items page')
def step_impl(context):
    context.base_page.login(configReader.readConfig("user info", "email"),
                            configReader.readConfig("user info", "password"))
    context.home_page.access_page("Items")


@when(u'I click on New Item')
def step_impl(context):
    context.items_page.click_new_item()


@when(u'fill new item Name as "{name}"')
def step_impl(context, name):
    context.items_page.type_item_name(name)


@when(u'fill new item Height as "{height}')
def step_impl(context, height):
    context.items_page.type_item_height(height)


@when(u'fill new item Width as "{width}"')
def step_impl(context, width):
    context.items_page.type_item_width(width)


@when(u'fill new item Weight as "{weight}"')
def step_impl(context, weight):
    context.items_page.type_item_weight(weight)


@when(u'I click on  Create Item')
def step_impl(context):
    context.items_page.create_new_item()
    assert context.items_page.is_item_created_msg() == "Item was successfully created."


@then(u'I see the item in items list "{name}""{height}""{width}""{weight}"')
def step_impl(context, name, height, width, weight):
    context.items_page.back_to_items()
    assert context.items_page.is_item_created(name)
    assert context.items_page.is_item_created(height)
    assert context.items_page.is_item_created(width)
    assert context.items_page.is_item_created(weight)


@when(u'I click on "{old_name}" to show the item data')
def step_impl(context, old_name):
    context.items_page.click_show_item_for_item(old_name)


@when(u'I click to edit the item')
def step_impl(context):
    context.items_page.edit_item()


@when(u'And I click to destroy the item')
def step_impl(context):
    context.items_page.destroy_item()


@then(u'I do not see "{name}" item in items list')
def step_impl(context, name):
    context.items_page.is_item_destroyed(name)
