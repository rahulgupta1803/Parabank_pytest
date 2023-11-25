import time

from pageobjects.register_page import Register
from utilities.register_logger import LogGenerator


class Test_Register():
    log = LogGenerator.loggen()

    def test_register(self,setup):
        self.driver = setup
        self.log.info("Open browser")
        self.rp = Register(self.driver)
        self.rp.Register_Button()
        self.log.info("Click on Register")
        self.rp.Enter_First_Name('Rahul')
        self.log.info("Enter First-Name")
        self.rp.Enter_Last_Name("Gupta")
        self.log.info("Enter Last-Name")
        self.rp.Enter_Address('hd-169,Sudama Nagar')
        self.log.info("Enter Address")
        self.rp.Enter_City('Roorkee')
        self.log.info("Enter City")
        self.rp.Enter_State('Uttarakhand')
        self.log.info("Enter State")
        self.rp.Enter_Zip('246778')
        self.log.info("Enter Zip")
        self.rp.Enter_Phone('6549871236')
        self.log.info("Enter Phone number")
        self.rp.Enter_SSN('2546')
        self.log.info("Enter SSN")
        self.rp.Enter_Username('rahul1234')
        self.log.info("Enter username")
        self.rp.Enter_Password('rahul@#$%')
        self.log.info("Enter Password")
        self.rp.Enter_Confirm_Password('rahul@#$%')
        self.log.info("Enter confirm-password")
        self.rp.Click_Confirm()
        self.log.info("Click confirm button")
        if  self.rp.Status()==True:
            print("Registration is complete")
            self.log.info("Registration is completed\n")
            time.sleep(2)
            self.driver.save_screenshot(".//screenshots//successful_registration.PNG")
            assert True
        else:
            print("Registration is failed")
            self.log.info("Registration is failed\n")
            time.sleep(2)
            self.driver.save_screenshot(".//screenshots//Failed_registration.PNG")
            assert False


# pytest -v -s --browser chrome "D:\credence\Parabank_pytest_project\testcases\test_register.py" --html=HTML_reports/register.html
