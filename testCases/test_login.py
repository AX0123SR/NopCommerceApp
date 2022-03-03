import time

import pytest
import sys
from selenium import webdriver

# To avoid ModuleError, use sys.path
sys.path.append("C://Users//ayussriv//PycharmProjects//NopCommerceApp")
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()


    def test_HomepageTitle(self,setup):
        self.logger.info("************* Test_001_Login *************")
        self.logger.info("************* Verifying HomePage title ************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("************* HomePage title verified *********** ")
            self.driver.close()

        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_HomepageTitle.png")
            self.driver.close()
            assert False
            self.logger.error("************* Homepage title is not matched *********** ")

    def test_login(self,setup):
        self.logger.info("************* Verifying LoginPage title *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* Loginpage title verified *********** ")
            self.driver.close()

        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            assert False
            self.logger.error("************* LoginPage title is not matched *********** ")


