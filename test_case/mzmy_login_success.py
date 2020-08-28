# coding=utf-8
from selenium import webdriver
import time
import unittest
from page.mzmy_login_page import LoginPage


class CaseLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.lp = LoginPage(self.driver)

    def test_Login_success(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp.send_username("18180470015")
        self.lp.send_password("123456")
        self.lp.click_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
