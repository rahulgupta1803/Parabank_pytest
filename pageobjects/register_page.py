from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Register():
    click_register_button_LINK_TEXT = (By.LINK_TEXT,"Register")
    text_first_name_ID = (By.ID,"customer.firstName")
    text_last_name_ID = (By.ID, "customer.lastName")
    text_address_ID = (By.ID, "customer.address.street")
    text_city_ID = (By.ID, "customer.address.city")
    text_state_ID = (By.ID, "customer.address.state")
    text_zip_ID = (By.ID, "customer.address.zipCode")
    text_phone_ID = (By.ID, "customer.phoneNumber")
    text_SSN_ID = (By.ID, "customer.ssn")
    text_username_ID = (By.ID, "customer.username")
    text_password_ID = (By.ID, "customer.password")
    text_confirm_password_ID = (By.ID, "repeatedPassword")
    click_confirm_button_XPATH = (By.XPATH,'//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
    status_XPATH = (By.XPATH,'//*[@id="leftPanel"]/ul/li[8]/a')

    def __init__(self,driver):
        self.driver = driver
        # self.wait=WebDriverWait(self.driver,20,poll_frequency=)

    def Register_Button(self):
        self.driver.find_element(*Register.click_register_button_LINK_TEXT).click()

    def Enter_First_Name(self,fname):
        self.driver.find_element(*Register.text_first_name_ID).send_keys(fname)

    def Enter_Last_Name(self,lname):
        self.driver.find_element(*Register.text_last_name_ID).send_keys(lname)
        # self.wait.until(expected_conditions.)

    def Enter_Address(self,address):
        self.driver.find_element(*Register.text_address_ID).send_keys(address)

    def Enter_City(self,city):
        self.driver.find_element(*Register.text_city_ID).send_keys(city)

    def Enter_State(self,state):
        self.driver.find_element(*Register.text_state_ID).send_keys(state)

    def Enter_Zip(self,zip):
        self.driver.find_element(*Register.text_zip_ID).send_keys(zip)

    def Enter_Phone(self,phone):
        self.driver.find_element(*Register.text_phone_ID).send_keys(phone)

    def Enter_SSN(self,ssn):
        self.driver.find_element(*Register.text_SSN_ID).send_keys(ssn)

    def Enter_Username(self,username):
        self.driver.find_element(*Register.text_username_ID).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*Register.text_password_ID).send_keys(password)

    def Enter_Confirm_Password(self,conf_password):
        self.driver.find_element(*Register.text_confirm_password_ID).send_keys(conf_password)

    def Click_Confirm(self):
        self.driver.find_element(*Register.click_confirm_button_XPATH).click()

    def Status(self):
        try:
            self.driver.find_element(*Register.status_XPATH)
            return True
        except:
            return False















