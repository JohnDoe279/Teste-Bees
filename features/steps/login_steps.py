from behave import *
from faker import Faker

fake = Faker()
email = fake.email()
password = "Teste@123"


@given(u'that I am in login page')
def step_impl(context):
    assert context.login_page.get_page_title() == "Test Bees"


@when(u'I click on Sign up button')
def step_impl(context):
    context.login_page.click_sign_up()


@when(u'fill the sign up form')
def step_impl(context):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    context.login_page.confirm_password(password)


@when(u'click on Sign up button')
def step_impl(context):
    context.login_page.submit_form()


@then(u'the new user is registered')
def step_impl(context):
    assert context.login_page.is_welcome_message_displayed()


@when(u'I enter my credential and submit')
def step_impl(context):
    context.base_page.login(email, password)


@then(u'i am logged in')
def step_impl(context):
    assert context.login_page.is_sign_in_message_displayed()


