from browser import Browser
from pages.base_page import Base_page
from pages.error_pass_page import Home_page
from pages.url_page import Url_page
from pages.email_page import Sign_up_page
from pages.incorrect_pass_page import Incorrect_pass

def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.url_object = Url_page()
    context.verify_object = Base_page()
    context.sign_up_object = Sign_up_page()
    context.incorrect_object = Incorrect_pass()

def after_all(context):
    context.browser.close()
