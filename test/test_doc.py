# -*- coding: utf-8 -*-
'''
==================================================
  @Time : 2021/3/24 9:30
  @Auth : Hua_
  @File : test_doc.py
  @IDE  : PyCharm
  @Motto: 人生苦短，我学Python！
  @Email: 1403589704@qq.com
==================================================
'''
import pytest
from common.handle_log import do_log
from pages.home_page import HomePage


class TestDoc:

    def test_adddoc(self, login):
        """新建doc功能"""

        try:
            driver = login
            home_page = HomePage(driver)
            home_page.get()
            res = home_page.find_open()
            expect = "开始"
            assert expect == res
        except Exception as e:
            do_log.error(f"测试用例不通过:{e}")
            raise e


if __name__ == '__main__':

    pytest.main(["-s", 'test_doc.py'])
