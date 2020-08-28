# coding=utf-8
from base.mzmy_base_page import BasePage


class LoginPage:

    def __init__(self, driver):
        self.bp = BasePage(driver)

    # 输入用户名
    def send_username(self, username):
        return self.bp.find_xpath("//input[@type='text']").send_keys(username)

    # 输入密码
    def send_password(self, password):
        return self.bp.find_xpath("//input[@type='password']").send_keys(password)

    # 点击登录按钮
    def click_button(self):
        return self.bp.find_xpath("//button[@type='button']").click()
