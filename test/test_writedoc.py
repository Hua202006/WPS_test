# -*- coding: utf-8 -*-
'''
==================================================
  @Time : 2021/3/24 10:23
  @Auth : Hua_
  @File : test_writedoc.py
  @IDE  : PyCharm
  @Motto: 人生苦短，我学Python！
  @Email: 1403589704@qq.com
==================================================
'''

from common.handle_log import do_log
from pages.home_page import HomePage
import pytest


class TestWritedoc:
    @pytest.mark.success
    def test_writedoc(self, login):
        """写入doc"""

        try:
            driver = login

            home_page = HomePage(driver)
            home_page.get()
            res = home_page.write_doc()
            expect = "Hello123"
            assert expect in res
        except Exception as e:
            do_log.error(f"测试用例不通过:{e}")
            raise e


if __name__ == '__main__':
    import pytest

    pytest.main(["-s", "test_writedoc.py"])
