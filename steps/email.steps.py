from behave import*

@when(u'Sign_in: I click on the sign_up button')
def step_impl(context):
    context.sign_up_object.navigate_to_sign_up_page()


@when(u'Sign_up: I click personal radio button')
def step_impl(context):
    context.sign_up_object.click_personal_button()


@when(u'Sign_up: I click continue button')
def step_impl(context):
    context.sign_up_object.click_continue_button()


@when(u'Sign_up: I send first name "Ramona"')
def step_impl(context):
    context.sign_up_object.send_firt_name('Ramona')


@when(u'Sign_up: I click continue first name button')
def step_impl(context):
    context.sign_up_object.click_continue_first_name_button()


@when(u'Sign_up: I send last name "Radu"')
def step_impl(context):
    context.sign_up_object.send_last_name('Radu')


@when(u'Sign_up: I click continue last name button')
def step_impl(context):
    context.sign_up_object.click_continue_last_name_button()


@when(u'Sign_up: I set my email to "ramo"')
def step_impl(context):
    context.sign_up_object.send_email('ramo')


@when(u'Sign_up: I receive message: Please enter a valid email address')
def step_impl(context):
    context.sign_up_object.receive_message()


@when(u'Sign_up: I clear the email textbox')
def step_impl(context):
    context.sign_up_object.clear_the_textbox()


@when(u'Sign_up: I put the correct email')
def step_impl(context):
    context.sign_up_object.send_the_correct_mail()


@then(u'Sign_up: I verify that error is not displayed anymore')
def step_impl(context):
    context.sign_up_object.verify_that_the_error_disappeared()

