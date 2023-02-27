from behave import *

@when ('Home page: Click on Sign up')
def step_impl(context):
    context.url_object.click_on_sign_up()

@then ('Sing-up page: Verify the excepted_url "https://jules.app/sign-up"')
def step_impl(context):
    context.verify_object.verify_url('https://jules.app/sign-up')

@when ('Sing-up page: Click on Log in')
def step_impl(context):
    context.url_object.click_on_log_in()

@then ('Home page: Verify the expected_url "https://jules.app/sign-in"')
def step_impl(context):
    context.verify_object.verify_url('https://jules.app/sign-in')



