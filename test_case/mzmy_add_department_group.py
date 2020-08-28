from selenium import webdriver
import time
import csv
import unittest
import login
from page.mzmy_add_department_group_page import AddDepartmentGroupPage
from page.mzmy_login_page import LoginPage


class AddDepartmentGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddDepartmentGroupPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_department_group(self):
        u"""添加部门分组"""
        with open("D:\\mzmy\\add_csv\\add_department_group.csv") as adg:
            adg = csv.reader(adg)
            for a in adg:
                if a[0] == "部门名称":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入基础类型设置
                    self.apt.click01()
                    self.apt.click02()
                    self.apt.click03()
                    # 新增部门分组
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.click06()
                    self.apt.click07()
                    self.apt.click08()
                    self.apt.send09(a[0])
                    self.apt.click10()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
