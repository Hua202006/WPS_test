"""配置。

yaml vs py ？？
- yaml, 通用的配置格式。 python, java, PHP, Go
- py, 在 python 项目中读取更方便。
"""
# 隐式等待的时间
import os

IMPLICTLY_WAIT_TIMEOUT = 10

# host
login_url = 'https://account.wps.cn/?qrcode=kdocs&logo=kdocs&cb=https%3A%2F%2F' \
            'account.wps.cn%2Fapi%2Fv3%2Fsession%2Fcorrelate%2Fredirect%3Ft%3D16' \
            '16478433594%26appid%3D375024576%26cb%3Dhttps%253A%252F%252Fwww.kdocs.cn%252Fsing' \
            'leSign4CST%253Fcb%253Dhttps%25253A%25252F%25252Fwww.kdocs.cn%25252Flatest%25253Ffrom%25253Ddocs'


# root path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# excel_path
DATA_PATH = os.path.join(ROOT_PATH, 'data')

# image_path 保存截图的文件路径
IMG_PATH = os.path.join(ROOT_PATH, 'screenshot')
# TODO: 加显示等待定位 invalid 错误信息
pass
