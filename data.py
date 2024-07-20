# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class TestData:
    username = "Admin"
    password = "admin123"
    mydata="test"
    title="OrangeHRM"

# Python Class for Selenium Selectors
class TestSelectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    admin_model=    "//span[text()='Admin']"
    admin_locators= "//*[@class='oxd-main-menu']/li"
    login_admin="//*[@type='submit']"
    admin_login="//span[text()='Admin']"
    menu_locator="//*[@class='oxd-topbar-body']/nav/ul/li"
    forgot_pass="//*[text()='Forgot your password? ']"
    reset_option="//*[text()=' Reset Password ']"
    # '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'