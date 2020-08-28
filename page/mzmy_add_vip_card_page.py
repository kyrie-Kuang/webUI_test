# coding=utf-8
from base.mzmy_base_page import BasePage


class AddVipCardPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入会员卡管理
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/div").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/ul/a[4]/li/span").click()

    # 添加会员卡
    def click04(self):
        return self.bp.find_xpath("(//button[@type='button'])[3]").click()

    def click05(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def send06(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[2]").send_keys(value)

    def click07(self):
        return self.bp.find_xpath("(//input[@type='text'])[3]").click()

    def send08(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[3]").send_keys(value)

    def click09(self):
        return self.bp.find_xpath("//div[7]/div[2]/div/div/div[3]/div/button[2]").click()
