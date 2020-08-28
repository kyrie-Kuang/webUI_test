#coding=utf-8
from selenium import webdriver
import time
def Login(self):

    #登录
    driver = self.driver
    driver.get("https://boss.meizitop.com/#/login")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@type='text']").clear()
    driver.find_element_by_xpath("//input[@type='text']").send_keys("18180470015")
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
    driver.find_element_by_xpath("//button[@type='button']").click()
    time.sleep(3)
