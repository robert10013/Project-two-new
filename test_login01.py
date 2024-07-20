import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import data
import pytest

class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        # service_obj = Service("c:/NewDriver/chromedriver.exe")
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    

    def test_mainmeu(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        username_field = self.driver.find_element(By.NAME, data.TestSelectors.input_box_username)
        username_field.send_keys(data.TestData.username)
        password_field = self.driver.find_element(By.NAME, data.TestSelectors.input_box_password)
        password_field.send_keys(data.TestData.password)
        login_button = self.driver.find_element(By.XPATH, data.TestSelectors.login_xpath)
        login_button.click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)
        admin_module = wait.until(EC.element_to_be_clickable((By.XPATH, data.TestSelectors.admin_model)))
        time.sleep(10)
        admin_module.click()
        self.driver.implicitly_wait(10)

        menu_link_locator = (By.XPATH,data.TestSelectors.admin_locators )
        menu_links = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(menu_link_locator))

        for link in menu_links:
            if link.is_displayed():
                print(f"Main Menu option '{link.text}' is displayed.")
            else:
                print(f"Main Menu option'{link.text}' is not displayed.")

    def test_header_admin(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        username_field = self.driver.find_element(By.NAME, data.TestSelectors.input_box_username)
        username_field.send_keys(data.TestData.username)
        password_field = self.driver.find_element(By.NAME, data.TestSelectors.input_box_password)
        password_field.send_keys(data.TestData.password)
        login_button = self.driver.find_element(By.XPATH, data.TestSelectors.login_admin)
        login_button.click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)
        admin_module = wait.until(EC.element_to_be_clickable((By.XPATH, data.TestSelectors.admin_login)))
        time.sleep(10)
        admin_module.click()
        self.driver.implicitly_wait(10)
        title = self.driver.title
        expected_title = (data.TestData.title)

        if title == expected_title:
            print(f"Title validation successful. Expected: '{expected_title}', Actual: '{title}'")
        else:
            print(f"Title validation failed. Expected: '{expected_title}', Actual: '{title}'")

        menu_link_locator = (By.XPATH, data.TestSelectors.menu_locator)
        menu_links = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(menu_link_locator))
        # Validate each menu link is displayed
        for link in menu_links:
            if link.is_displayed():
                print(f"Admin Page text '{link.text}' is displayed.")
            else:
                print(f"Admin Page text '{link.text}' is not displayed.")

    def test_ForgotPassword(self, booting_function):
        self.driver.get(self.url)
        time.sleep(10)
        forgot_password_link = self.driver.find_element(By.XPATH, data.TestSelectors.forgot_pass)
        forgot_password_link.click()

        time.sleep(5)

        wait = WebDriverWait(self.driver, 10)
        username_field = self.driver.find_element(By.NAME, data.TestSelectors.input_box_username)
        username_field.send_keys(data.TestData.mydata)

        reset_link = self.driver.find_element(By.XPATH, data.TestSelectors.reset_option)
        reset_link.click()
        time.sleep(10)
        print("Reset Password link sent successfully.")


