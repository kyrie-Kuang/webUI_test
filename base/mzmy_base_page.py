# -*- coding: utf-8 -*-
'''
相关功能：用来存放定位最基础的页面元素方法
'''


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_xpath(self, value):
        return self.driver.find_element_by_xpath(value)
