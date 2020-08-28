# coding=utf-8
from base.mzmy_base_page import BasePage


class SinglePayment:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 选择单个服务项目支付
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/a/li/span").click()

    # 选择服务项目
    def click03(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def click04(self):
        return self.bp.find_xpath("//span/form/div/div/div/label").click()

    def click05(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def click06(self):
        return self.bp.find_xpath("//div[10]/div/span/form/div/div/div/label").click()

    # 添加，选择服务项目
    def click07(self):
        return self.bp.find_xpath("//div[6]/div/button").click()

    def click08(self):
        return self.bp.find_xpath("//div[2]/div/div/div/div/div[3]/button[2]").click()

    def click09(self):
        return self.bp.find_xpath("//div[16]/button").click()

    def click10(self):
        return self.bp.find_xpath("(//button[@type='button'])[21]").click()

    def click11(self):
        return self.bp.find_xpath("//div[14]/div/span/form/div/div/div/label").click()

    # 结算
    def click12(self):
        return self.bp.find_xpath("//div[6]/div/button").click()

    def click13(self):
        return self.bp.find_xpath("//div[2]/div/div/div/div/div[3]/button[2]").click()

    def click14(self):
        return self.bp.find_xpath("//div[16]/button").click()

    def click15(self):
        return self.bp.find_xpath("(//button[@type='button'])[21]").click()
