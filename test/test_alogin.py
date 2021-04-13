"""doc文档输入文字功能"""

import pytest
from common.handle_log import do_log
from data.login_data import login_error
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:

    # @pytest.mark.skip(reason='不执行登录失败用例')  # 运行时跳过此用例，不执行。
    @pytest.mark.login
    @pytest.mark.error
    @pytest.mark.parametrize("test_info", login_error)
    def test_login_error(self, browser, test_info):
        """登录失败"""

        try:
            login_page = LoginPage(browser)

            login_page.get().login(test_info["user"], test_info["password"])
            res = login_page.login_error_text()
            expect = "帐号或密码不正确"
            assert expect in res
        except Exception as e:
            do_log.error(f"测试用例不通过:{e}")
            raise e

    @pytest.mark.success
    @pytest.mark.login
    def test_login(self, login):
        """登录成功"""

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

    pytest.main(["-s", "-m", "login"])
