# coding=utf-8
from base.mzmy_base_page import BasePage


class AddPackagePage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入基础类型设置
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/div").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[2]/ul/a[3]/li").click()

    # 新增套餐
    def click04(self):
        return self.bp.find_xpath("(//button[@type='button'])[3]").click()

    def click05(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def send06(self, value):
        return self.bp.find_xpath("//input[@type='text']").send_keys(value)

    def click07(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def send08(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[2]").send_keys(value)

    def click09(self):
        return self.bp.find_xpath("//div[3]/div/div/div/span").click()

    def click10(self):
        return self.bp.find_xpath("//li/li").click()

    def click11(self):
        return self.bp.find_xpath("//div[4]/div/div/div/div/i").click()

    def click12(self):
        return self.bp.find_xpath("//span[5]/em").click()

    def click13(self):
        return self.bp.find_xpath("//div[5]/div/div/div/div/i").click()

    def click14(self):
        return self.bp.find_xpath("//div[5]/div/div/div[2]/div/div/div[2]/div/span[5]/em").click()

    def click15(self):
        return self.bp.find_xpath("//div[10]/label").click()

    def click16(self):
        return self.bp.find_xpath("//td/div/div/button").click()

    def click17(self):
        return self.bp.find_xpath("//span/ul/li").click()

    def click18(self):
        return self.bp.find_xpath("//div/div/label/span/input").click()

    def click19(self):
        return self.bp.find_xpath("//div[7]/div[2]/div/div/div[3]/div/button[2]").click()
