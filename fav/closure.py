# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


"""
闭包定义
1. 内层函数引用了自由变量
2. 外部函数返回内部函数名

代码判断
1. func.__code__.co_freevars
2. func.__closure__
"""

"""
def func(arg):
    def inner(arg):
        return arg
    return inner

No
"""

"""
def func(arg):
    def inner(a):
        return arg
    return inner

Yes
"""


"""
def func(arg):
    def inner(arg):
        return 5
    return inner

No
"""

"""
def func(name):
    log(name)

    def inner(arg):
        return arg
    return inner

No
"""

"""
def func(arg):
    return lambda x: x + arg

Yes
"""

"""
def func(arg):
    return lambda x: x + 1

No
"""

"""
def numFunc(a, b):
    num = 100
    num2 = 200
    num3 = 300

    def addfunc(a, b):
        s = 'string in addfunc' + str(a)
        x = num
        y = num3

    return addfunc

num num2 num3 都是自由变量
但是 addfunc 只引用了 num num3
"""


# if __name__ == '__main__':
#     log(func(1).__closure__)
#     log(func(1).__code__.co_freevars)
