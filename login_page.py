# pages/login_page.py
from pytest import Config
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def navigate_to_login_page(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "txtUsername").send_keys(username)
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()
