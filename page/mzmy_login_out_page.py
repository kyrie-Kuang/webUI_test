# coding=utf-8
from base.mzmy_base_page import BasePage


class LoginOutPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    def click01(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div/div[2]/div[2]/div[4]/span/div/div/a/span[2]").click()

    def click02(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div/div[2]/div[2]/div[4]/span/div/div[2]/ul/span[2]/li/span").click()
