# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 函数的参数传递的是内存地址/引用

# v = [11, 22, 33]
#
#
# def func(arg):
#     log(id(arg))
#
#
# log(id(v))
# func(v)
"""
4431645384
4431645384
"""


# def func():
#     log(x)
#
#
# func()


def func(arg):
    return lambda x: x + arg


# log(func(5).__code__.co_freevars)
# log(func(5).__closure__)
"""
('arg',)
(<cell at 0x102994eb8: int object at 0x10265d840>,)
func 是闭包
"""


def func1():
    return lambda x: x + 1


# log(func1().__code__.co_freevars)
# log(func1().__closure__)
"""
()
None
func1 不是闭包
"""


def func2():
    def inner():
        pass
    return inner


# log(func2().__code__.co_freevars)
# log(func2().__closure__)
"""
()
None
不是闭包
"""


# def wrapper(func):
#     log(123)
#
#     def inner():
#         return func()
#     return inner
#
#
# @wrapper
# def index():
#     return 5


# log(index.__code__.co_freevars)
# log(index.__closure__)


# a = [i if i > 5 else 0 for i in range(10)]
# log(a)


# a = [i for i in range(10) if i > 5]
# log(a)
