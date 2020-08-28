# coding=utf-8
from selenium import webdriver
import time
import unittest
import login
from page.mzmy_change_password_page import ChangePwdPage
from page.mzmy_login_page import LoginPage


class ChangePassword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.cpp = ChangePwdPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_change_password(self):
        u"""修改密码"""

        # self.driver = webdriver.Firefox()
        # #登录
        # login.Login(self)
        # #修改密码
        # driver = self.driver

        self.driver.get(self.url)
        self.driver.maximize_window()
        # 登陆
        self.lp.send_username("18180470015")
        self.lp.send_password("123456")
        self.lp.click_button()
        # 修改密码
        self.cpp.click01()
        self.cpp.click02()
        self.cpp.send01("123456")
        self.cpp.send02("123456")
        self.cpp.send03("123456")
        self.cpp.click03()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
