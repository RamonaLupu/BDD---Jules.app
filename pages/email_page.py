import time
from pages.base_page import Base_page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException

class Sign_up_page(Base_page):
    SIGN_UP = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    PERSONAL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[1]/span/input')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]')
    FIRST_NAME = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    FIRST_NAME_CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')
    LAST_NAME =(By.XPATH, '//*[@placeholder = "Type your answer here..."]')
    LAST_NAME_CONTINUE_BUTTON = (By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[3]/button/span[1]')
    EMAIL = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    RECEIVE_MESSAGE = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')



    def navigate_to_sign_in_page(self):
        self.chrom.get ('https://jules.app/')

    def navigate_to_sign_up_page(self):
        self.chrom.find_element(*self.SIGN_UP).click()
        time.sleep(3)

    def click_personal_button(self):
        self.chrom.find_element(*self.PERSONAL_BUTTON).click()
        time.sleep(3)

    def click_continue_button(self):
        self.chrom.find_element(*self.CONTINUE_BUTTON).click()

    def send_firt_name(self, name):
        self.chrom.find_element(*self.FIRST_NAME).send_keys(name)
        time.sleep(3)

    def click_continue_first_name_button(self):
        self.chrom.find_element(*self.FIRST_NAME_CONTINUE_BUTTON).click()
        time.sleep(3)

    def send_last_name(self, last_name):
        self.chrom.find_element(*self.LAST_NAME).send_keys(last_name)
        time.sleep(5)

    def click_continue_last_name_button(self):
        self.chrom.find_element(*self.LAST_NAME_CONTINUE_BUTTON).click()
        time.sleep(5)

    def send_email(self, email):
        self.chrom.find_element(*self.EMAIL).send_keys(email)
        time.sleep(3)

    def receive_message(self):
        message = self.chrom.find_element(*self.RECEIVE_MESSAGE).text
        expected_message = 'Please enter a valid email address.'
        assert message == expected_message, f'Error email address {message} is not {expected_message}'

    def clear_the_textbox(self):
        self.chrom.find_element(*self.EMAIL).send_keys(Keys.CONTROL, "a")
        self.chrom.find_element(*self.EMAIL).send_keys(Keys.BACKSPACE)
        time.sleep(5)

    def send_the_correct_mail(self):
        self.chrom.find_element(*self.EMAIL).send_keys('raduramona86@yahoo.com')
        time.sleep(5)

    def verify_that_the_error_disappeared(self):
        try:
            self.chrom.find_element(*self.RECEIVE_MESSAGE)
        except NoSuchElementException:
            return True




