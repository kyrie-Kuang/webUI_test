# coding=utf-8
from base.mzmy_base_page import BasePage


class ChangePwdPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    def click01(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div/div[2]/div[2]/div[4]/span/div/div/a/span[2]").click()

    def click02(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div/div[2]/div[2]/div[4]/span/div/div[2]/ul/span/li/span").click()

    def send01(self, pwd01):
        return self.bp.find_xpath("//input[@type='password']").send_keys(pwd01)

    def send02(self, pwd02):
        return self.bp.find_xpath("(//input[@type='password'])[2]").send_keys(pwd02)

    def send03(self, pwd03):
        return self.bp.find_xpath("(//input[@type='password'])[3]").send_keys(pwd03)

    def click04(self):
        return self.bp.find_xpath("(//button[@type='button'])[4]").click()
