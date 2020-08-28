from selenium import webdriver
import unittest
import time
import csv
import HTMLTestRunner
import io
import login
from page.mzmy_add_service_project_page import AddServiceProjectPage
from page.mzmy_login_page import LoginPage


class AddServiceProject(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "https://boss.meizitop.com/#/login"
        self.apt = AddServiceProjectPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_add_service_project(self):
        u"""添加服务项目"""
        # 读取csv文件数据
        with open("D:\\mzmy\\add_csv\\add_service_project.csv") as asp:
            asp = csv.reader(asp)
            for a in asp:
                if a[0] == "项目名称":
                    continue
                else:
                    self.driver.get(self.url)
                    self.driver.maximize_window()
                    # 登陆
                    self.lp.send_username("18180470015")
                    self.lp.send_password("123456")
                    self.lp.click_button()
                    # 进入服务项目界面
                    self.apt.click01()
                    self.apt.click02()
                    self.apt.click03()
                    # 新增服务项目
                    self.apt.click04()
                    self.apt.click05()
                    self.apt.send06(a[0])
                    self.apt.click07()
                    self.apt.click08()
                    self.apt.send09(a[1])
                    self.apt.click10()
                    self.apt.click11()
                    self.apt.click12()
                    self.apt.click13()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
    # #定义一个单元测试容器
    # testunit = unittest.TestSuite()

    # #将测试用例添加到测试容器中

    # testunit.addTest(UntitledTestCase("test_more_add_service_project"))

    # #定义报告存放路径
    # filename = "D:\\mzmy\\add_service_project\\result.html"

    # fn = open(filename,"wb")

    # #定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(

    #     stream = fn,
    #     title = u"服务项目新增报告",
    #     description = u"用例执行情况:"
    #     )

    # #运行测试用例
    # runner.run(testunit)
