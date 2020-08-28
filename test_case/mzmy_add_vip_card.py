from selenium import webdriver
import time
import csv
import unittest
import login
from page.mzmy_add_vip_card_page import AddVipCardPage
from page.mzmy_login_page import LoginPage


class AddVipCard(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddVipCardPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_vip_card(self):
        u"""添加会员卡"""
        with open("D:\\mzmy\\add_csv\\add_vipcard.csv") as avc:
            avc = csv.reader(avc)
            for a in avc:
                if a[0] == "会员卡编号":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入会员卡管理
                    self.apt.click01()
                    self.apt.click02()
                    self.apt.click03()
                    # 添加会员卡
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send06(a[0])
                    self.apt.click07()
                    self.apt.send08(a[1])
                    self.apt.click09()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
