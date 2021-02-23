# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   BeginningPython
@File       :   Ch09.py
@Version    :   v0.1
@Time       :   2021-02-23 9:35
@License    :   (C)Copyright 2018-2021, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from tools import beep_end


# ----------------------------------------------------------------------
def main():
    import random
    pretty_print(random.choice(list(queens())))
    # print(list(queens(4, (1, 3, 0))))
    # print(list(queens(6, (1, 3, 0, 2, 4))))
    pass


def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


def conflict(state, nextX):
    # nextX：表示下一个皇后的水平位置
    # nextY：表示下一个皇后的垂直位置
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


if __name__ == '__main__':
    main()
    beep_end()
