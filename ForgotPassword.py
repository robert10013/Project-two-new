from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.maximize_window()
driver.implicitly_wait(10)

forgot_password_link = driver.find_element(By.XPATH, "//*[text()='Forgot your password? ']")
forgot_password_link.click()


time.sleep(5)

wait = WebDriverWait(driver, 10)
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("test")

reset_link = driver.find_element(By.XPATH, "//*[text()=' Reset Password ']")
reset_link.click()
time.sleep(10)
print("Reset Password link sent successfully.")


# Close the browser
driver.quit()