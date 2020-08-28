# coding=utf-8
from base.mzmy_base_page import BasePage


class AddManagerPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入管理员设置
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[6]/div/span").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[6]/ul/a/li/span").click()

    # 添加管理员
    def click04(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/div[3]").click()

    def click05(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def send06(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[2]").send_keys(value)

    def click07(self):
        return self.bp.find_xpath("(//input[@type='password'])[4]").click()

    def send08(self, value):
        return self.bp.find_xpath("(//input[@type='password'])[4]").send_keys(value)

    def click09(self):
        return self.bp.find_xpath("(//input[@type='text'])[3]").click()

    def send10(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[3]").send_keys(value)

    def click11(self):
        return self.bp.find_xpath("//form/div[5]/div/div/div/span").click()

    def click12(self):
        return self.bp.find_xpath("//div[7]/ul[2]/li").click()

    def click13(self):
        return self.bp.find_xpath("//div[6]/div/div/div/span").click()

    def click14(self):
        return self.bp.find_xpath("//div[8]/ul[2]/li").click()

    def click15(self):
        return self.bp.find_xpath("//div[9]/div[2]/div/div/div[3]/div/button[2]").click()
