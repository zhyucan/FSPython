# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 1.
# 写出三元运算的基本格式及作用？


# 2.
# 什么是匿名函数？


# 3.
# 尽量多的列举你了解的内置函数？【默写】


# 4.
# filter / map / reduce函数的作用分别是什么？


# 5.
# 看代码写结果
# def func(*args, **kwargs):
#     print(args, kwargs)
#
#
# a. 执行 func(12,3,*[11,22]) ，输出什么？
# b. 执行 func(('alex','武沛齐',),name='eric')
# func(12, 3, *[11, 22])
# func(('alex', '武沛齐',), name='eric')
"""
(12, 3, 11, 12) {}
(('alex', '武沛齐'),) {'name': 'eric'}
"""


# 6.
# 看代码分析结果
# def func(arg):
#     return arg.pop(1)
#
#
# result = func([11, 22, 33, 44])
# print(result)
"""
22
"""


# 7.
# 看代码分析结果
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda: i)
#
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1, v2)
"""
9 9
"""


# 8.
# 看代码分析结果
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1, v2)
"""
11 10
"""


# 9.
# 看代码分析结果
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# for i in range(0, len(func_list)):
#     result = func_list[i](i)
#     print(result)
"""
0
2
4
...
18
"""


# 10.
# 看代码分析结果
# def f1():
#     print('f1')
#
#
# def f2():
#     print('f2')
#     return f1
#
#
# func = f2()
# result = func()
# print(result)
"""
f2
f1
None
"""


# 11.
# 看代码分析结果【面试题】
# def f1():
#     print('f1')
#     return f3()
#
#
# def f2():
#     print('f2')
#     return f1
#
#
# def f3():
#     print('f3')
#
#
# func = f2()
# result = func()
# print(result)
"""
f2
f1
f3
None
"""


# 12.
# 看代码分析结果
# name = '景女神'
#
#
# def func():
#     def inner():
#         print(name)
#
#     return inner()
#
#
# v = func()
# print(v)
"""
景女神
None
"""


# 13.
# 看代码分析结果
# name = '景女神'
#
#
# def func():
#     def inner():
#         print(name)
#         return "老男孩"
#
#     return inner()
#
#
# v = func()
# print(v)
"""
景女神
老男孩
"""


# 14.
# 看代码分析结果
# name = '景女神'
#
#
# def func():
#     def inner():
#         print(name)
#         return '老男孩'
#
#     return inner
#
#
# v = func()
# result = v()
# print(result)
"""
景女神
老男孩
"""


# 15.
# 看代码分析结果
# def func():
#     name = '武沛齐'
#
#     def inner():
#         print(name)
#         return '老男孩'
#
#     return inner
#
#
# v1 = func()()
# v2 = func()()
# print(v1, v2)
"""
武沛齐
武沛齐
老男孩 老男孩
"""


# 16.
# 看代码写结果
# def func(name):
#     def inner():
#         print(name)
#         return '老男孩'
#
#     return inner
#
#
# v1 = func('金老板')()
# v2 = func('alex')()
# print(v1, v2)
"""
金老板
alex
老男孩 老男孩
"""


# 17.
# 看代码写结果
# def func(name=None):
#     if not name:
#         name = '武沛齐'
#
#     def inner():
#         print(name)
#         return '老男孩'
#
#     return inner
#
#
# v1 = func()()
# v2 = func('alex')()
# print(v1, v2)
"""
武沛齐
alex
老男孩 老男孩
"""


# 18.
# 看代码写结果【面试题】
# def func(name):
#     return lambda x: x + name
#
#
# v1 = func('武沛齐')
# v2 = func('alex')
# v3 = v1('银角')
# v4 = v2('金角')
# print(v1, v2, v3, v4)
"""
<lambda> <lambda> 银角武沛齐 金角alex
"""


# 19.
# 看代码写结果
# NUM = 100
# result = []
# for i in range(10):
#     func = lambda: NUM  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
"""
9
[lambda: 100, ..., lambda: 100]
100 100
"""


# 20.
# 看代码写结果【面试题】
# result = []
# for i in range(10):
#     func = lambda: i  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
"""
9
[lambda: 9, ..., lambda: 9]
9 9
"""


# 21.
# 看代码分析结果【面试题】
# def func(num):
#     def inner():
#         print(num)
#
#     return inner
#
#
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
"""
9
[<func>, ..., <func>]
0
9
None None
"""


# 22.
# 程序设计题
#
# 请设计实现一个商城系统，商城主要提供两个功能：商品管理、会员管理。
#
# 商品管理：
# - 查看商品列表
# - 根据关键字搜索指定商品
# - 录入商品
#
# 会员管理：【无需开发，如选择则提示此功能不可用，正在开发中，让用户重新选择】
#
# 需求细节：
# 1. 启动程序让用户选择进行商品管理或会员管理
# 2. 用户选择【1】则进入商品管理页面，进入之后显示商品管理相关的菜单
# 3. 用户选择【2】则提示此功能不可用，正在开发中，让用户重新选择。
# 4. 如果用户在【商品管理】中选择【1】，则按照分页去文件 goods.txt
# 中读取所有商品，并全部显示出来【分页功能可选】。
# 5. 如果用户在【商品管理】中选择【2】，则让提示让用户输入关键字，
# 输入关键字后根据商品名称进行模糊匹配
# 6. 如果用户在【商品管理】中选择【3】，则提示让用户输入商品名称、价格、数量
# 然后写入到 goods.txt 文件
class Good:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.number = num


# goods_list = []

# with open('goods.txt') as f:
#     for line in f:
#         name, price, num = line.strip().split('|')
#         good = Good(name, price, num)
#         goods_list.append(good.__dict__)


def split_pages(lst, num):
    d, m = divmod(len(lst), num)
    for i in range(d+1):
        log('*** page {} ***'.format(i+1))
        for j in lst[i*num:i*num+num]:
            log('{} {} {}'.format(j['name'], j['price'], j['number']))


def match(lst, s):
    for i in lst:
        if s in i['name']:
            log('{} {} {}'.format(i['name'], i['price'], i['number']))


while 1:
    user = input("""
    ******欢迎使用购物商城******
    1. 商品管理
    2. 会员管理（不可选，正在开发中）

    请选择（输入 N 返回上一级）: """).strip()

    with open('goods.txt') as f:
        goods_list = []
        for line in f:
            name, price, num = line.strip().split('|')
            good = Good(name, price, num)
            goods_list.append(good.__dict__)

    if user == 'N':
        break
    elif not user.isdecimal():
        log('请按要求输入')
    elif int(user) == 1:
        while 1:
            choice = input("""
            ******欢迎使用购物商城[商品管理]******
            1. 查看商品列表
            2. 根据关键字搜索指定商品
            3. 录入商品

            请选择（输入 N 返回上一级）: """).strip()
            if choice == 'N':
                break
            elif not user.isdecimal():
                log('请按要求输入')
            elif int(choice) == 1:
                page = int(input('page_num: '))
                split_pages(goods_list, page)
            elif int(choice) == 2:
                s = input('search: ')
                match(goods_list, s)
            elif int(choice) == 3:
                pass
            else:
                log('请按要求输入')
    elif int(user) == 2:
        log('此功能不可用，请重新选择')
        continue
    else:
        log('请按要求输入')
