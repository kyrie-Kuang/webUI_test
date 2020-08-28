from selenium import webdriver
import unittest
import time
import csv
import HTMLTestRunner
import io
import login
from page.mzmy_more_add_permission_group_page import AddPermissionGroupPage
from page.mzmy_login_page import LoginPage


class AddPermissionGroup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddPermissionGroupPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_more_add_permission_group(self):
        u"""添加权限组"""
        # 读取csv文件数据
        with open("D:\\mzmy\\add_csv\\add_permission_group.csv") as apg:
            apg = csv.reader(apg)
            for a in apg:
                if a[0] == "权限组名称":
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
                    # 添加权限组
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send01(a[0])
                    self.apt.click06()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
