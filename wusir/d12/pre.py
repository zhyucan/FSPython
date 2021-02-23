# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# def func(a=123, b):
#     return a + b
#
#
# func(5)


"""
函数从创建它的作用域开始执行
执行时开辟的内存空间属于创建它的作用域
"""

# name = 'alex'
#
#
# def base():
#     log(name)
#
#
# def func():
#     name = 'eric'
#     base()
#
#
# func()
"""
base 执行时，会在创建它的全局作用域开辟内存空间
而不是 func 的局部作用域
"""


# name = 'alex'
#
#
# def base(name):
#     log(name)
#
#
# def func():
#     name = 'eric'
#     base(name)
#
#
# func()


# name = 'alex'
#
#
# def func():
#     name = 'eric'
#
#     def base():
#         log(name)
#
#     base()
#
#
# func()


# name = 'alex'
#
#
# def func():
#     name = 'eric'
#
#     def base():
#         log(name)
#
#     return base
#
#
# func()()
