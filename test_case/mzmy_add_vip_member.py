from selenium import webdriver
import unittest
import csv
import time
import login
from page.mzmy_add_vip_member_page import AddVipMemberPage
from page.mzmy_login_page import LoginPage


class AddVipMember(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddVipMemberPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_vip_member(self):
        u"""添加会员"""
        with open("D:\\mzmy\\add_csv\\add_vip_member.csv") as avm:
            avm = csv.reader(avm)
            for a in avm:
                if a[0] == "会员编号":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入收银界面
                    self.apt.click01()
                    self.apt.click02()
                    # 添加会员
                    self.apt.click03()
                    self.apt.click04()
                    self.apt.send05(a[0])
                    self.apt.click06()
                    self.apt.send07(a[0])
                    self.apt.click08()
                    self.apt.send09(a[0])
                    self.apt.click10()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
