# coding=utf-8
from base.mzmy_base_page import BasePage


class AddPermissionGroupPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入管理员设置
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[6]/div/span").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[6]/ul/a/li/span").click()

    # 添加权限组
    def click04(self):
        return self.bp.find_xpath("(//button[@type='button'])[3]").click()

    def click05(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def send01(self, value):
        return self.bp.find_xpath("//input[@type='text']").send_keys(value)

    def click06(self):
        return self.bp.find_xpath("//div[6]/div[2]/div/div/div[3]/div/button[2]").click()
