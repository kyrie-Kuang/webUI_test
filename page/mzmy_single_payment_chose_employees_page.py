# coding=utf-8
from base.mzmy_base_page import BasePage


class SinglePaymentChoseEmployeesPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 单个服务项目，多个员工，支付
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/a/li/span").click()

    # 选择服务项目
    def click03(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def click04(self):
        return self.bp.find_xpath("//span/form/div/div/div/label").click()

    # 选择多个服务员工
    def click05(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def click06(self):
        return self.bp.find_xpath("//div[10]/div/span/form/div/div/div/label").click()

    def click07(self):
        return self.bp.find_xpath("(//button[@type='button'])[7]").click()

    def click08(self):
        return self.bp.find_xpath("(//input[@type='text'])[3]").click()

    def click09(self):
        return self.bp.find_xpath("//div[13]/div/span/form/div/div/div/label[2]").click()

    def click10(self):
        return self.bp.find_xpath("(//button[@type='button'])[7]").click()

    def click11(self):
        return self.bp.find_xpath("(//input[@type='text'])[4]").click()

    def click12(self):
        return self.bp.find_xpath("//div[15]/div/span/form/div[2]/div/div/label").click()

    # 结算
    def click13(self):
        return self.bp.find_xpath("//div[6]/div/button").click()

    def click14(self):
        return self.bp.find_xpath("//div[2]/div/div/div/div/div[3]/button[2]").click()

    def click15(self):
        return self.bp.find_xpath("//div[16]/button").click()

    def click16(self):
        return self.bp.find_xpath("(//button[@type='button'])[21]").click()
