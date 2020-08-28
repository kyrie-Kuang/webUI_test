# coding=utf-8
from base.mzmy_base_page import BasePage


class AddDepartmentGroupPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入基础类型设置
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/div").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/ul/a/li").click()

    # 新增部门分组
    def click04(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[3]").click()

    def click05(self):
        return self.bp.find_xpath("(//button[@type='button'])[3]").click()

    def click06(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def click07(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def click08(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def send09(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[2]").send_keys(value)

    def click10(self):
        return self.bp.find_xpath("//div[6]/div[2]/div/div/div[3]/div/button[2]").click()
