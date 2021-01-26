# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   BeginningPython
@File       :   Ch03.py
@Version    :   v0.1
@Time       :   2020-12-25 17:58
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from math import pi

from tools import beep_end
from tools import show_subtitle


def sec01():
    website = "https://zhuyuanxiang.github.io"
    print(website[8:20])
    # website[8:20]="yuanxiangzhu" # Error
    pass


def sec02():
    show_subtitle("简化说明符")
    fmt_str = "Hello, %s. %s enough for ya?"
    values = ('world', 'Hot')
    print(fmt_str % values)
    show_subtitle("模板字符串")
    from string import Template
    tmpl = Template("Hello, $who! $what enough for ya?")
    print(tmpl.substitute(who="Mars", what="Dusty"))
    pass


def sec03():
    # 如何设置格式的信息使用一种微型格式指定语言(mini-language)。
    # 每个值都被插入到字符串中，以替换用花括号括起来的替换字段。
    # 使用两个 花括号 可以插入花括号
    print("{{ceci n'est pas une replacement field}}".format())
    # 替换字段名
    print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))
    print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))
    # 导入变量
    fullname = ['Alfred', 'Smoketoomuch']
    print("Mr {name[1]}".format(name=fullname))
    # 导入模块
    import math
    tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
    print(tmpl.format(mod=math))
    show_subtitle("表3-1 字符串格式设置中的类型说明符")
    # 转换标志：s 代表 str；r 代表 repr；a 代表 ascii
    # 函数 str 创建外观普通的字符串版本
    # 函数 repr 创建给定值的 Python 表示
    # 函数 ascii 创建只包含 ASCII 字符的表示
    print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
    # 字符 f ：表示定点数；字符 b : 表示二进制
    print("The number is {num}".format(num=42))
    print("The number is {num:f}".format(num=42))
    print("The number is {num:b}".format(num=42))
    # 设置显示内容的宽度
    print("-->{num:10} {num:10}<--".format(num=3))
    print("-->{name:10} {name:10}<--".format(name="Bob"))
    # 设置显示内容的精度
    print("0123456789012345678901234567890123456789")
    print("Pi day is {pi:.2f}".format(pi=pi))
    print("Pi day is {pi:10.2f}".format(pi=pi))
    # 对字符串指定精度
    print("{:.5}".format("Guido van Rossum"))
    # 使用逗号来添加 千位分隔符
    print("One googol iss {:,}".format(10 ** 100))
    # 使用 0 填充
    show_subtitle("填充")
    print("{:010.2f}".format(pi))
    print("{:010.2f}".format(-pi))
    print("{:+10.2f}".format(pi))
    print("{:+10.2f}".format(-pi))
    print("{:-10.2f}".format(pi))
    print("{:-10.2f}".format(-pi))
    print("{: 10.2f}".format(pi))
    # 指定：左对齐(<)、右对齐(>)、居中(^)
    show_subtitle("对齐")
    print("{0:<010.2f}\n{0:^010.2f}\n{0:>010.2f}".format(pi))
    print("{:$^15}".format(" WIN BIG "))
    # 说明符(=)：将填充字符放在符号和数字之间
    print("{0:10.2f}\t{1:10.2f}".format(pi, -pi))
    print("{0:10.2f}\t{1:=10.2f}".format(pi, -pi))
    # 说明符：-、+、空格
    print("{0:.2}\t{1:.2}".format(pi, -pi))
    print("{0:-.2}\t{1:-.2}".format(pi, -pi))  # 默认设置
    print("{0:+.2}\t{1:+.2}".format(pi, -pi))
    print("{0: .2}\t{1: .2}".format(pi, -pi))
    # 井号(#)：为数字进制转换加上前缀
    print("{:b}".format(42))
    print("{:#b}".format(42))
    print("{:o}".format(42))
    print("{:#o}".format(42))
    print("{:x}".format(42))
    print("{:#x}".format(42))
    # 对于十进制数，保留小数点
    print("{:g}".format(0x2a))
    print("{:#g}".format(0x2a))


# ----------------------------------------------------------------------
def code3_1():
    width = int(input("Please enter width: "))
    price_width = 10
    item_width = width - price_width
    header_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
    fmt = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)
    print('=' * width)
    print(header_fmt.format('Item', 'Price'))
    print('-' * width)
    print(fmt.format('Apples', 0.4))
    print(fmt.format('Pears', 0.5))
    print(fmt.format('Cantaloupes', 1.92))
    print(fmt.format('Dried Apricots (16 oz.)', 8))
    print(fmt.format('Prunes (4 lbs.)', 12))
    print('=' * width)

    pass


def main():
    # sec01()
    # sec02()
    # sec03()
    code3_1()
    pass


if __name__ == '__main__':
    main()
    beep_end()
