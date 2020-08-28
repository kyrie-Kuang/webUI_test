# coding=utf-8
from base.mzmy_base_page import BasePage


class AddVipMemberPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入收银界面
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a/li").click()

    def click02(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/a/div/div/div/div").click()

    # 添加会员
    def click03(self):
        return self.bp.find_xpath("(//button[@type='button'])[3]").click()

    def click04(self):
        return self.bp.find_xpath("(//input[@type='text'])[4]").click()

    def send05(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[4]").send_keys(value)

    def click06(self):
        return self.bp.find_xpath("(//input[@type='text'])[5]").click()

    def send07(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[5]").send_keys(value)

    def click08(self):
        return self.bp.find_xpath("(//input[@type='text'])[6]").click()

    def send09(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[6]").send_keys(value)

    def click10(self):
        return self.bp.find_xpath("(//button[@type='button'])[15]").click()
