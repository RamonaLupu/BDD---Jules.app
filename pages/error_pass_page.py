import time
from selenium.webdriver.common.keys import Keys

from pages.base_page import Base_page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Home_page(Base_page):
    EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASS = (By.XPATH, "//input[@placeholder='Enter your password']")
    ERROR_MESSAGE =(By.XPATH, '//p[text()="Please enter your password!"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'css-17qmje5')


    def navigate_to_jules_app(self):
        self.chrom.get('https://jules.app/')


    def input_email(self):
        self.chrom.find_element(*self.EMAIL).send_keys('raduramona86@yahoo.com')


    def leave_password_empty(self):
        self.chrom.find_element(*self.PASS).send_keys('3')
        self.chrom.find_element(*self.PASS).send_keys(Keys.CONTROL, 'a')
        self.chrom.find_element(*self.PASS).send_keys(Keys.BACKSPACE)


    def verify_error(self):
        assert self.chrom.find_element(*self.ERROR_MESSAGE).is_displayed(), f'Error: The error message is not displayed'

    def verify_LOGIN_button(self):
        assert self.chrom.find_element(*self.LOGIN_BUTTON).is_enabled(), f'Error: The log in button is not enabled'
