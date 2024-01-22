# pages/pim_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):
    def navigate_to_pim_module(self):
        self.driver.find_element(By.ID, "menu_pim_viewPimModule").click()

    def add_new_employee(self, first_name, last_name):
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "btnSave").click()

    def edit_employee(self, employee_id, new_first_name):
        # Navigate to the employee list
        self.driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()

        # Search for the employee to be edited
        self.driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(employee_id)
        self.driver.find_element(By.ID, "searchBtn").click()

        # Click on the employee in the search results
        self.driver.find_element(By.XPATH, f"//a[text()='{employee_id}']").click()

        # Edit the employee's information
        self.driver.find_element(By.ID, "btnSave").click()
        self.driver.find_element(By.ID, "firstName").clear()
        self.driver.find_element(By.ID, "firstName").send_keys(new_first_name)
        self.driver.find_element(By.ID, "btnSave").click()

    def delete_employee(self, employee_id):
        # Navigate to the employee list
        self.driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()

        # Search for the employee to be deleted
        self.driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(employee_id)
        self.driver.find_element(By.ID, "searchBtn").click()

        # Click on the checkbox next to the employee in the search results
        self.driver.find_element(By.XPATH, f"//a[text()='{employee_id}']/../../td[1]/input").click()

        # Click on the "Delete" button
        self.driver.find_element(By.ID, "btnDelete").click()

        # Confirm the deletion
        self.driver.find_element(By.ID, "dialogDeleteBtn").click()
