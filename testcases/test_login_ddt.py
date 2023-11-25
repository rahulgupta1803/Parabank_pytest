from pageobjects.login_page import Login
from utilities import xlutilis
from utilities.register_logger import LogGenerator


class Test_Login_DDT():
    fpath = "D:\\credence\\Parabank_pytest_project\\testcases\\testdata\\login_data.xlsx"
    log=LogGenerator.loggen()
    def test_login_ddt(self,setup):
        self.driver = setup
        self.log.info("Opening browser")
        self.lp = Login(self.driver)
        rl= xlutilis.RowCount(self.fpath,'Sheet1')
        print(rl)
        status_list = []
        for r in range(2,rl+1):
            username = xlutilis.ReadData(self.fpath,'Sheet1',r,2)
            password = xlutilis.ReadData(self.fpath,'Sheet1',r,3)
            exp_result = xlutilis.ReadData(self.fpath,'Sheet1',r,4)
            self.lp.Enter_Username(username)
            self.log.info("Enter Username")
            self.lp.Enter_Password(password)
            self.log.info("Enter Password")
            self.lp.Click_Login()
            self.log.info("Click login")
            if self.lp.Status() == True:
                status_list.append('pass')
                xlutilis.WriteData(self.fpath, 'Sheet1', r, 5, 'pass')
                self.driver.save_screenshot(f".\\screenshots\\{username}_{password}.png")
                self.log.info("Take screenshot")
                if exp_result=='pass':
                    xlutilis.WriteData(self.fpath,'Sheet1',r,6,'pass')
                else:
                    xlutilis.WriteData(self.fpath, 'Sheet1', r, 6, 'fail')
                self.lp.Click_Logout()
                self.log.info("Click Logout")

            elif self.lp.Status() == False:
                xlutilis.WriteData(self.fpath, 'Sheet1', r, 5, 'fail')
                status_list.append('fail')
                self.driver.save_screenshot(f".\\screenshots\\{username}_{password}.png")
                self.log.info("Take screenshot")
                if exp_result == 'pass':
                    xlutilis.WriteData(self.fpath, 'Sheet1', r, 5, 'fail')
                else:
                    xlutilis.WriteData(self.fpath, 'Sheet1', r, 5, 'pass')

        print(status_list)
        if 'fail' not in status_list:
            self.log.info("Test is passed\n")
            assert True

        else:
            self.log.info("Test is failed\n")
            assert False



# pytest -v -s --browser chrome "D:\credence\Parabank_pytest_project\testcases\test_login_ddt.py" --alluredir="D:\credence\Parabank_pytest_project\allure-results"






