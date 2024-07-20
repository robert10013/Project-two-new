from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)


username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")
login_button = driver.find_element(By.XPATH, "//*[@type='submit']")
login_button.click()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
admin_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
time.sleep(10)
admin_module.click()
driver.implicitly_wait(10)

menu_link_locator = (By.XPATH, "//*[@class='oxd-main-menu']/li")
menu_links = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(menu_link_locator))

for link in menu_links:
    if link.is_displayed():
        print(f"Main Menu option '{link.text}' is displayed.")
    else:
        print(f"Main Menu option'{link.text}' is not displayed.")

# Close the browser
driver.quit()