"""收集和运行用例。"""

import pytest

'''
#生成html报告
import os
from datetime import datetime
from common.handle_path import REPORTS_PATH
from common.handle_yaml import do_yaml

html_filename = do_yaml.get_data('report', 'filename') + '_' + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + ".html"  #实时生成测试报告
html_filename = os.path.join(REPORTS_PATH, html_filename)
pytest.main([f'--html={html_filename}'])
'''

pytest.main(['-s', '--alluredir=reports/', '--clean-alluredir', '--reruns=2', '--reruns-delay=3'])  # 生成allure报告
# 每次运行pytest.main, 将报告放到reports路径；清楚之前报告记录；重运行进制2次,延时3秒运行
