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

pytest.main(['-s','--alluredir=reports/','--clean-alluredir']) #生成allure报告

