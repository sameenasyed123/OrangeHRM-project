# tests/test_login.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.test_login import LoginPage
from utils.config import Config

class TestLogin(pytest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login("Admin", "admin123")
        self.assertIn("Dashboard", self.driver.title)

    def test_invalid_login(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login("Admin", "InvalidPassword")
        self.assertIn("Invalid credentials", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()
