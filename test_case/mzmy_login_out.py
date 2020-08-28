# coding=utf-8
from selenium import webdriver
import time
import unittest
import login
from page.mzmy_login_out_page import LoginOutPage
from page.mzmy_login_page import LoginPage


class LoginOut(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.lop = LoginOutPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_login_out(self):
        u"""注销"""

        # self.driver = webdriver.Firefox()
        # #登录
        # login.Login(self)
        # driver = self.driver

        self.driver.get(self.url)
        self.driver.maximize_window()
        # 登陆
        self.lp.send_username("18180470015")
        self.lp.send_password("123456")
        self.lp.click_button()
        # 注销用户
        self.lop.click01()
        self.lop.click02()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
