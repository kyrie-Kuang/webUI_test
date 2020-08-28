from selenium import webdriver
import time
import csv
import unittest
import login
from page.mzmy_add_package_page import AddPackagePage
from page.mzmy_login_page import LoginPage


class Add_Package(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddPackagePage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_package(self):
        u"""添加套餐"""
        with open("D:\\mzmy\\add_csv\\add_package.csv") as adg:
            adg = csv.reader(adg)
            for a in adg:
                if a[0] == "套餐编号":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入疗程套餐界面
                    self.apt.click01()
                    self.apt.click02()
                    self.apt.click03()
                    # 新增套餐
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send06(a[0])
                    self.apt.click07()
                    self.apt.send08(a[1])
                    self.apt.click09()
                    self.apt.click10()
                    self.apt.click11()
                    self.apt.click12()
                    self.apt.click13()
                    self.apt.click14()
                    # 使用JS脚本，将滚动条拖到指定地方
                    target = self.apt.click15()
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    self.apt.click16()
                    self.apt.click17()
                    self.apt.click18()
                    self.apt.click19()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
