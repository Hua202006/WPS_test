from common.handle_log import do_log
import os
import time


from selenium.webdriver import Chrome,Firefox
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import config

from datetime import datetime


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def find(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
        except Exception as err:
            # 没有找到元素
            do_log.error(f"元素定位失败：{err}")
            self.save_screenshot()
        else:
            return e

    def save_screenshot(self):
        """截屏"""
        # 获取路径
        img_path = config.IMG_PATH
        # 生成截图的文件名时间戳
        ts_str = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        file_name = os.path.join(img_path, ts_str + ".png")
        self.driver.save_screenshot(file_name)
        return self

    def find_and_red(self, locator):
        """定位元素并且标成红色.。 装饰器实现。"""
        try:
            e = self.driver.find_element(*locator)
            # js 指令改变该元素的背景色。 border
            js_code = "arguments[0].style.borderColor='red';"
            self.driver.execute_script(js_code, e)

        except Exception as err:
            do_log.error(f"元素定位失败：{err}")
        else:
            return e

    def wait_element_clickable(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可以被点击"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.element_to_be_clickable(locator))
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")
        else:
            return e

    def wait_element_visible(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可见"""

        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.visibility_of_element_located(locator))
            return e
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")

    def wait_element_present(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素被加载"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.presence_of_element_located(locator))
            return e
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")

    def click_element(self, locator):
        """点击某个元素"""
        try:
            e = self.wait_element_clickable(locator)
            e.click()
            return self
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")


    def double_click(self, locator):
        """双击某个元素"""
        try:
            e = self.wait_element_clickable(locator)
            ac = ActionChains(self.driver)
            ac.double_click(e).perform()
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")
        else:
            return self

    def move_to(self, locator):
        """鼠标悬停"""
        try:
            e = self.wait_element_clickable(locator)
            ac = ActionChains(self.driver)
            ac.move_to_element(e).perform()
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")
        else:
            return self

    def switch_to_frame(self, e, wait=False):
        """iframe 切换"""
        try:
            if not wait:
                self.driver.switch_to.frame(e)
                return self
            wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(e))
            return self
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")

    def switch_to_alert(self):
        """切换到弹窗"""
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.alert_is_present())  # 等待弹窗出现
            alert = self.driver.switch_to.alert  # 先切换到弹框的
            alert.accept()  # 确认
            # text=alert.text()  #获取弹窗文本内容
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"元素定位失败：{err}")
        else:
            return alert

    def switch_to_window(self):
        """ 窗口切换到最新的窗口 """
        handles = self.driver.window_handles  # 获取浏览器当前打开的窗口数
        try:
            WebDriverWait(self.driver, 30, 1).until(expected_conditions.new_window_is_opened(handles))  # 等待新窗口出现
            self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到新窗口
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"窗口切换失败：{err}")
        else:
            return self

    def window_scroll(self, width=None, height=None):
        """ 滑动到窗口 -设置窗口滚动条的宽度和高度 """
        try:
            if width is None:
                width = "0"
            if height is None:
                height = "0"
            js = "window.scrollTo({w},{h});".format(w=width, h=height)
            self.driver.execute_script(js)
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"窗口滚动失败：{err}")
        else:
            return self


    def file_upload(self,locator,file_path):
        ''' 文件上传 '''
        try:
            mfile = self.find(locator)
            # 点击
            mfile.click()
            # #方法2 python3.8有异常
            time.sleep(2)
            import pyautogui
            pyautogui.write(file_path)
            time.sleep(2)
            pyautogui.press('enter', 2)
            time.sleep(3)

            ##方法1
            #from pywinauto import Desktop
            # from pywinauto import Desktop
            # app = Desktop()
            # # 窗口
            # dialog = app['打开']  # 根据名字找到弹出窗口
            # # 窗口上的控件
            # time.sleep(1)
            # dialog["Edit"].type_keys(file_path)  # 在输入框中输入值
            # time.sleep(2)
            # dialog["Button"].click()
            # time.sleep(2)
            #1/文件上传失败时，强制等待时间可以增多去调试验证; 2/打断点时需要断点到上传后打，否则有可能失败
        except Exception as err:
            self.save_screenshot()
            do_log.error(f"上传文件失败：{err}")
        else:
            return self

