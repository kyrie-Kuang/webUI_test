# coding=utf-8
from base.mzmy_base_page import BasePage


class AddServiceProjectPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入服务项目界面
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/div").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/ul/a[2]/li/span").click()

    # 新增服务项目
    def click04(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def click05(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def send06(self, value):
        return self.bp.find_xpath("//input[@type='text']").send_keys(value)

    def click07(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def click08(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def send09(self, value):
        return self.bp.find_xpath("//input[@type='text']").send_keys(value)

    def click10(self):
        return self.bp.find_xpath("//div[3]/div/div/div/span").click()

    def click11(self):
        return self.bp.find_xpath("//li/li").click()

    def click12(self):
        return self.bp.find_xpath("(//input[@type='checkbox'])[12]").click()

    def click13(self):
        return self.bp.find_xpath("//div[6]/div[2]/div/div/div[3]/div/button[2]").click()
