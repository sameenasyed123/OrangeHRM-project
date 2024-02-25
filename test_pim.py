# tests/test_pim.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.test_login import LoginPage
from tests.test_pim import PIMPage
from utils.config import Config

class TestPIM(pytest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.login_page = LoginPage(self.driver)
        self.pim_page = PIMPage(self.driver)

    def test_add_edit_delete_employee(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login("Admin", "admin123")

        # Navigate to PIM module
        self.pim_page.navigate_to_pim_module()

        # Add a new employee
        self.pim_page.add_new_employee("John", "Doe")

        # Edit the added employee
        self.pim_page.edit_employee("John Doe", "UpdatedJohn")

        # Delete the edited employee
        self.pim_page.delete_employee("UpdatedJohn")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()
