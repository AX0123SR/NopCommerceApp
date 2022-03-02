import time

import pytest
import sys
from selenium import webdriver

# To avoid ModuleError, use sys.path
sys.path.append("C://Users//ayussriv//PycharmProjects//NopCommerceApp")
from pageObjects.LoginPage import LoginPage



class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "//input[@class = 'email']"
    password = "//input[@class = 'password']"

    def test_HomepageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_HomepageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            assert False

