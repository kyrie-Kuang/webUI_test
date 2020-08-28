from selenium import webdriver
import unittest
import time
import csv
import HTMLTestRunner
import io
import login
from page.mzmy_add_manager_page import AddManagerPage
from page.mzmy_login_page import LoginPage


class AddManager(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddManagerPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_manager(self):
        u"""添加管理员"""
        # 读取csv文件数据
        with open("D:\\mzmy\\add_csv\\add_manager.csv") as am:
            am = csv.reader(am)
            for a in am:
                if a[0] == "手机号":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入管理员设置
                    self.apt.click01()
                    self.apt.click02()
                    self.apt.click03()
                    # 添加管理员
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send06(a[0])
                    self.apt.click07()
                    self.apt.send08(a[0])
                    self.apt.click09()
                    self.apt.send10(a[0])
                    self.apt.click11()
                    self.apt.click12()
                    self.apt.click13()
                    self.apt.click14()
                    self.apt.click15()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
