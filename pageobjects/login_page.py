from selenium.webdriver.common.by import By


class Login():
    text_username_NAME = (By.NAME,'username')
    text_password_NAME = (By.NAME,'password')
    click_login_XPATH = (By.XPATH,'//*[@id="loginPanel"]/form/div[3]/input')
    status_XPATH = (By.XPATH, '//*[@id="leftPanel"]/ul/li[8]/a')
    click_logout_XPATH = (By.XPATH,'//*[@id="leftPanel"]/ul/li[8]/a')

    def __init__(self,driver):
        self.driver = driver

    def Enter_Username(self,username):
        self.driver.find_element(*Login.text_username_NAME).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*Login.text_password_NAME).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Login.click_login_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*Login.click_logout_XPATH).click()

    def Status(self):
        try:
            self.driver.find_element(*Login.status_XPATH)
            return True
        except:
            return False