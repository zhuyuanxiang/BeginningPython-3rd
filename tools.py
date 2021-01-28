# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   BeginningPython
@File       :   tools.py
@Version    :   v0.1
@Time       :   2020-12-25 18:00
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""


def show_subtitle(message):
    # 输出运行模块的子标题
    print('-' * 15, '>' + message + '<', '-' * 15)
    pass


def show_title(message):
    # 输出运行模块的子标题
    print()
    print('=' * 15, '>' + message + '<', '=' * 15)
    pass


def beep_end():
    # 运行结束的提醒
    import winsound
    winsound.Beep(600, 500)
    pass
