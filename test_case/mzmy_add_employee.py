# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import csv
import unittest
import login
from page.mzmy_add_employee_page import AddEmployeePage
from page.mzmy_login_page import LoginPage


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddEmployeePage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_employee(self):
        u"""添加员工"""
        with open("D:\\mzmy\\add_csv\\add_employee.csv", "r", encoding="gbk") as ae:
            ae = csv.reader(ae)
            for a in ae:
                if a[0] == "姓名":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入员工界面
                    self.apt.click01()
                    self.apt.click02()
                    self.apt.click03()
                    # 新增员工
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send06(a[0])
                    self.apt.click07()
                    self.apt.click08()
                    self.apt.click09()
                    self.apt.click10()
                    self.apt.click11()
                    self.apt.send12(a[1])
                    self.apt.click13()
                    self.apt.send14(a[2])
                    self.apt.click15()
                    self.apt.send16(a[3])
                    self.apt.click17()
                    self.apt.send18(a[4])
                    self.apt.click19()
                    self.apt.send20(a[5])
                    self.apt.click21()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
