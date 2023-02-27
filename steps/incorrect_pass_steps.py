from behave import *

@when(u'Home page: I input the correct email')
def step_impl(context):
    context.incorrect_object.input_email()


@when(u'Home page: I put the incorrect password')
def step_impl(context):
    context.incorrect_object.input_incorrect_password()


@then(u'Home page: Verify error ‘Invalid email/password combination’ is displayed')
def step_impl(context):
    context.incorrect_object.verify_error_message()


@then(u'Home page: Verify Log in btn is displayed')
def step_impl(context):
    context.incorrect_object.verify_LOGIN_button()
