# -*- coding: utf-8 -*-
'''
==================================================
  @Time : 2021/3/23 14:43
  @Auth : Hua_
  @File : home_page.py
  @IDE  : PyCharm
  @Motto: 人生苦短，我学Python！
  @Email: 1403589704@qq.com
==================================================
'''
from common.base_page import BasePage
from config import config


class HomePage(BasePage):
    url = 'https://www.kdocs.cn/p/109021460010'
    new_locator = ("xpath", "//div[@class='add-file-btn']//div")
    open_locator = ('xpath', "//div[@id='StartTab']")
    write_locator = ('xpath', "//input[@class='virtual-input no-public-autofocus']")
    page_text_locator = ('xpath', "//*[@class='text-page']")
    insert_locator=('xpath',"//div[@id='InsertTab']")
    picture_locator = ('xpath', '//div[text()="图片"]')
    file_path = r'C:\Users\zh\Desktop\Linux.png'
    img_path=('xpath','//*[@id="image"]')

    def find_data(self):
        """获取新建按钮的文本"""
        e = self.wait_element_visible(self.new_locator)
        return e.text

    def get(self):
        """进入页面"""
        self.driver.get(self.url)
        return self

    def find_open(self):
        '''获取 开始 按钮文本'''
        e = self.wait_element_visible(self.open_locator)
        return e.text

    def write_doc(self):
        '''在doc文档添加文字并返回文本内容'''
        e = self.find(self.write_locator)
        e.send_keys('Hello123')
        ele = self.find(self.page_text_locator)
        return ele.text

    def add_picture(self):
        """插入图片"""
        e=self.find(self.insert_locator)
        e.click()
        self.file_upload(self.picture_locator)
        if self.find(self.img_path):
            return "图片插入成功"
        else:
            return "图片插入失败"