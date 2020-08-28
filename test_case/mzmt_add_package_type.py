# coding=utf-8
from selenium import webdriver
import time
import io
import csv
import unittest
import HTMLTestRunner
import login
from page.mzmy_add_package_type_page import AddPackageTypePage
from page.mzmy_login_page import LoginPage


class AddPackageType(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddPackageTypePage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_package_type(self):
        u"""添加套餐类型"""
        with open("E:\\mzmy\\csv_add\\add_package_type.csv") as apt:
            apt = csv.reader(apt)
            for a in apt:
                if a[0] == "类型名称":
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
                    # 新增套餐类型
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send01(a[0])
                    self.apt.click06()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
    # #定义单元测试容器
    # testunit = unittest.TestSuite()

    # #将用例添加到容器中
    # testunit.addTest(AddPackageType("test_more_add_package_type"))

    # #定义存放路径
    # filename = "D:\\mzmy\\add_package_type\\result.html"

    # fn = open(filename,"wb")

    # #定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream = fn,
    #     title = u"套餐类型测试报告",
    #     description = u"用例执行情况"

    #     )

    # runner.run(testunit)
