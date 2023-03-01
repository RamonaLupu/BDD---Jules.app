

from browser import Browser
from selenium.webdriver.common.by import By

class Base_page(Browser):
    EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    PASS = (By.XPATH, "//input[@placeholder='Enter your password']")
    LOGIN_BUTTON = (By.CLASS_NAME, 'MuiButton-label')


    def verify_url(self, expected_url):
        url = self.chrom.current_url
        assert url == expected_url, f'Error: Url {url} is different from the expected url {expected_url}'

