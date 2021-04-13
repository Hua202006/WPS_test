# -*- coding: utf-8 -*-
'''
==================================================
  @Time : 2021/3/23 14:16
  @Auth : Hua_
  @File : login_page.py
  @IDE  : PyCharm
  @Motto: 人生苦短，我学Python！
  @Email: 1403589704@qq.com
==================================================
'''
import time

from common.base_page import BasePage
from config import config


class LoginPage(BasePage):
    url = config.login_url
    # 元素定位
    more_locator = ('xpath', "//a[@class='js_toProtocolDialog more']//span[1]")
    agree_locator = ('xpath', "//div[@class='dialog-footer-ok']")
    user_and_pwdlocator = ("xpath", "//span[@id='account']//span[2]")
    user_locator = ("xpath", "//input[@id='email']")
    pwd_locator = ('xpath', "//input[@id='password']")
    confirm_locator = ("xpath", "//div[@id='rectBottom']")
    login_locator = ("xpath", "//a[@id='login']")
    login_error_locator = ('xpath', "//span[@id='errorMsg']")

    def get(self):
        """访问login页面"""
        self.driver.get(self.url)
        return self

    def login(self, user, pwd):
        """登录操作"""
        self.click_element(self.more_locator)  # 点击更多
        self.click_element(self.agree_locator)  # 点击同意
        self.click_element(self.user_and_pwdlocator)  # 点击账号密码登录
        ele = self.find(self.user_locator)
        ele.send_keys(user)
        ele_01 = self.find(self.pwd_locator)
        ele_01.send_keys(pwd)
        self.click_element(self.confirm_locator)
        time.sleep(5)
        self.click_element(self.login_locator)

        return self

    def login_error_text(self):
        """ 获取登录失败文本"""
        e = self.wait_element_visible(self.login_error_locator)
        return e.text

