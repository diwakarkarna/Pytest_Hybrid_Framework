import pytest
from selenium import webdriver
from pageobjects.login import LoginPage


class Test001Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homepageTitle.png")
            #self.driver.close
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administrationd":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            #self.driver.close
            assert False
