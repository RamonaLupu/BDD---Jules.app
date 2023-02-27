from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Browser():
    chrom = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    chrom.maximize_window()
    chrom.implicitly_wait(7)

    def close(self):
        self.chrom.delete_all_cookies()
        self.chrom.quit()