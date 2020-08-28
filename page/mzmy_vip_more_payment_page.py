# coding=utf-8
from base.mzmy_base_page import BasePage


class VipMorePaymentPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 会员购买项目
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/a/li/span").click()

    def click03(self):
        return self.bp.find_xpath("(//input[@type='radio'])[2]").click()

    def click04(self):
        return self.bp.find_xpath("//input[@type='text']").click()

    def send05(self, value):
        return self.bp.find_xpath("//input[@type='text']").send_keys(value)

    def click06(self):
        return self.bp.find_xpath(
            "//div[@id='app']/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/ul[2]/li/div/div[2]").click()

    # 选择多个项目
    def click07(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def click08(self):
        return self.bp.find_xpath("//span/form/div/div/div/label").click()

    def click09(self):
        return self.bp.find_xpath("(//input[@type='text'])[3]").click()

    def click10(self):
        return self.bp.find_xpath("//div[13]/div/span/form/div/div/div/label").click()

    def click11(self):
        return self.bp.find_xpath("(//button[@type='button'])[5]").click()

    def click12(self):
        return self.bp.find_xpath("(//input[@type='text'])[4]").click()

    def click13(self):
        return self.bp.find_xpath("//div[13]/div/span/form/div/div/div/label").click()

    def click14(self):
        return self.bp.find_xpath("(//input[@type='text'])[5]").click()

    def click15(self):
        return self.bp.find_xpath("//div[14]/div/span/form/div/div/div/label").click()

    # 结算
    def click16(self):
        return self.bp.find_xpath("//div[6]/div/button").click()

    def click17(self):
        return self.bp.find_xpath("//div[2]/div/div/div/div/div[3]/button[2]").click()

    def click18(self):
        return self.bp.find_xpath("//div[16]/button").click()

    def click19(self):
        return self.bp.find_xpath("(//button[@type='button'])[21]").click()
