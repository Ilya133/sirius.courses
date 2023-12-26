from selenium import webdriver
from selene import browser


class BrowserManager:

    def __init__(self):
        self.base_url = "https://uts.sirius.online//#/auth/register/qainternship"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')
        options.add_argument('--enable-automation')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-setuid-sandbox')
        browser.config.driver.maximize_window()
        browser.config.driver_options = options
        browser.config.timeout = 2

    def open(self):
        browser.open(self.base_url)

    def close(self):
        browser.close()
