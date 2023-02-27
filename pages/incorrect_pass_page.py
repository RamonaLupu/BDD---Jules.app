import time
from pages.base_page import Base_page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Incorrect_pass(Base_page):
    EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASS = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BUTTON = (By.CLASS_NAME, 'MuiButton-label')
    ERROR_INCORRECT_PASS = (By.XPATH, "//span[text()='Invalid email/password combination']")

    def input_email(self):
        self.chrom.find_element(*self.EMAIL).send_keys('raduramona86@yahoo.com')

    def input_incorrect_password(self):
        self.chrom.find_element(*self.PASS).send_keys('12345')


    def verify_error_message(self):
        self.chrom.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)
        expected_message = 'Invalid email/password combination'
        message = self.chrom.find_element(*self.ERROR_INCORRECT_PASS).text
        assert message == expected_message, f'Error: The error message is not the expected message'

    def verify_LOGIN_button(self):
        assert self.chrom.find_element(*self.LOGIN_BUTTON).is_displayed(), f'Error: The log in button is enabled'