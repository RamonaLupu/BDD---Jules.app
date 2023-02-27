from pages.base_page import Base_page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Url_page(Base_page):
    LOG_IN =(By.XPATH, "//span[text()='Log In.']")
    SIGN_UP = (By.XPATH, "//a[text()='Sign up.']")

    def click_on_sign_up(self):
        self.chrom.find_element(*self.SIGN_UP).click()

    # def verify_url(self,expected_url):
    #     pass

    def click_on_log_in(self):
        self.chrom.find_element(*self.LOG_IN).click()

    def verify_url(self, expected_url):
        pass


