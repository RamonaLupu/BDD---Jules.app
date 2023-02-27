from behave import *

@given ('Home page: Open jules.app')
def step_impl(context):
    context.home_page_object.navigate_to_jules_app()

@when ('Home page: Input correct email')
def step_impl(context):
    context.home_page_object.input_email()

@when ('Home page: Leave pass empty')
def step_impl(context):
    context.home_page_object.leave_password_empty()

@then ('Home page: Verify error ‘Please enter your password!’ is displayed')
def step_impl(context):
    context.home_page_object.verify_error()

@then ('Home page: Verify Log in btn is disabled')
def step_impl(context):
    context.home_page_object.verify_LOGIN_button()