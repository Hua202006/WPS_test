"""doc文档输入文字功能"""
import pytest
from common.handle_log import do_log
from pages.home_page import HomePage


class TestLogin:

    def test_login(self, login):
        """登录"""

        try:
            driver = login
            home_page = HomePage(driver)
            res = home_page.find_data()
            expect = "新 建"
            assert expect in res
        except Exception as e:
            do_log.error(f"测试用例不通过:{e}")
            raise e


if __name__ == '__main__':
    import pytest

    pytest.main(["-s"])
