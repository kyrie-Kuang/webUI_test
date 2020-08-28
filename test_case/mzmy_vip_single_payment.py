from selenium import webdriver
import unittest
import time
import login
from page.mzmy_login_page import LoginPage
from page.mzmy_vip_single_payment_page import VipSinglePaymentPage


class VipSinglePayment(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.mpp = VipSinglePaymentPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_vip_single_payment(self):
        u"""会员购买单个项目，选择单个员工"""
        for i in range(0, 1):
            self.driver.get(self.url)
            self.driver.maximize_window()
            # 登陆
            self.lp.send_username("18180470015")
            self.lp.send_password("123456")
            self.lp.click_button()
            # 会员购买项目
            self.mpp.click01()
            self.mpp.click02()
            self.mpp.click03()
            self.mpp.click04()
            self.mpp.send05("1")
            self.mpp.click06()
            # 选择单个项目
            self.mpp.click07()
            self.mpp.click08()
            self.mpp.click09()
            self.mpp.click10()
            self.mpp.click11()
            self.mpp.click12()
            self.mpp.click13()
            self.mpp.click14()
            self.mpp.click14()
            # 结算
            self.mpp.click15()
            self.mpp.click16()
            self.mpp.click17()
            self.mpp.click18()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
