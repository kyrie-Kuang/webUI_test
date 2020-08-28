# coding=utf-8
from selenium import webdriver
import time
import unittest
import login
from page.mzmy_more_payment_page import MorePaymentPage
from page.mzmy_login_page import LoginPage


class MorePayment(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.mpp = MorePaymentPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_more_payments(self):
        u"""多个服务项目支付"""

        for i in range(0, 2):
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
            # 选择多个服务项目支付
            self.mpp.click01()
            self.mpp.click02()
            # 选择服务项目
            self.mpp.click03()
            self.mpp.click04()
            self.mpp.click05()
            self.mpp.click06()
            # 添加，选择服务项目
            self.mpp.click07()
            self.mpp.click08()
            self.mpp.click09()
            self.mpp.click10()
            self.mpp.click11()
            # 结算
            self.mpp.click12()
            self.mpp.click13()
            self.mpp.click14()
            self.mpp.click15()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
