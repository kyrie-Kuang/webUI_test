# coding=utf-8
from base.mzmy_base_page import BasePage


class AddEmployeePage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 进入员工界面
    def click01(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div[2]/div/div/ul/div/a[3]/li").click()

    def click02(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[5]/div").click()

    def click03(self):
        return self.bp.find_xpath("//div[@id='app']/div/div/div/ul/li[5]/ul/a/li").click()

    # 新增套餐类型
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath().send_keys(a[0])
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(a[1])
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(a[2])
    driver.find_element_by_xpath().click()
    driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys(a[3])
    driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(a[4])
    driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(a[5])
    driver.find_element_by_xpath().click()

    def click04(self):
        return self.bp.find_xpath("(//button[@type='button'])[4]").click()

    def click05(self):
        return self.bp.find_xpath("(//input[@type='text'])[2]").click()

    def send06(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[2]").send_keys(value)

    def click07(self):
        return self.bp.find_xpath("//div[3]/div/div/div/span").click()

    def click08(self):
        return self.bp.find_xpath("//span/li[3]").click()

    def click09(self):
        return self.bp.find_xpath("//div[4]/div/div/div/span").click()

    def click10(self):
        return self.bp.find_xpath("//div[4]/div/div/div[2]/ul[2]/li").click()

    def click11(self):
        return self.bp.find_xpath("(//input[@type='text'])[3]").click()

    def send12(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[3]").send_keys(value)

    def click13(self):
        return self.bp.find_xpath("(//input[@type='text'])[4]").click()

    def send14(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[4]").send_keys(value)

    def click15(self):
        return self.bp.find_xpath("(//input[@type='text'])[6]").click()

    def send16(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[6]").send_keys(value)

    def click17(self):
        return self.bp.find_xpath("(//input[@type='text'])[7]").click()

    def send18(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[7]").send_keys(value)

    def click19(self):
        return self.bp.find_xpath("(//input[@type='text'])[8]").click()

    def send20(self, value):
        return self.bp.find_xpath("(//input[@type='text'])[8]").send_keys(value)

    def click21(self):
        return self.bp.find_xpath("(//div[8]/div[2]/div/div/div[3]/div/button[2])").click()
