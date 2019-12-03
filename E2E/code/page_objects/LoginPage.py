from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginPage:

    def __init__(self, driver: webdriver):
        try:
            self.driver = driver
            self.driver.implicitly_wait(10)  # seconds
            self.driver.get('https://www.saucedemo.com/')
            self.login_field = self.driver.find_element_by_id('user-name')
            self.password_field = self.driver.find_element_by_id('password')
            self.login_btn = self.driver.find_element_by_css_selector('.btn_action')
        except Exception:
            driver.close()

    def login(self, user, password):
        self.login_field.send_keys(user)
        self.password_field.send_keys(password)
        self.login_btn.click()

    def standard_login(self):
        self.login('standard_user', 'secret_sauce')
