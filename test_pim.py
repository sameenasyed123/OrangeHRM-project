# tests/test_pim.py
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from utils.config import Config

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
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
    unittest.main()
