# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# sys.path.append("/root/mods")的作用？
# 添加环境变量

# 字符串如何进行反转？
# s[::-1]


# 不用中间变量交换a和b的值。
#
# a = 1
# b = 2
# a, b = b, a


# *args和**kwargs这俩参数是什么意思？我们为什么要用它。


# 函数的参数传递是地址还是新值？
# 地址


# 看代码写结果：
# my_dict = {'a': 0, 'b': 1}
#
#
# def func(d):
#     d['a'] = 1
#     return d
#
#
# func(my_dict)
# my_dict['c'] = 2
# print(my_dict)
"""
{'a': 1, 'b': 1, 'c': 2}
"""


# 什么是lambda表达式


# range和xrang有什么不同？


# "1,2,3" 如何变成 ['1','2','3',]
# log('1,2,3'.split(','))


# ['1','2','3'] 如何变成 [1,2,3]
# log([int(i) for i in ['1','2','3']])


# def f(a,b=[]) 这种写法有什么陷阱？


# 如何生成列表 [1,4,9,16,25,36,49,64,81,100] ，尽量用一行实现。
# log([i*i for i in range(1, 11)])


# python一行print出1~100偶数的列表, (列表推导式, filter均可)
# l = filter(lambda i: i % 2 == 0, range(1, 101))
# log(list(l))


# 把下面函数改成lambda表达式形式
# def func():
#     result = []
#     for i in range(10):
#         if i % 3 == 0:
#             result.append(i)
#     return result
#
#
# f = lambda: [i for i in range(10) if i % 3 == 0]
# log(f())


# 如何用Python删除一个文件？
# import os
# os.remove('test')


# 如何对一个文件进行重命名？
# import os
# os.rename('test', 'tt')


# python如何生成随机数？
# import random
# for _ in range(10):
#     log(int(random.random() * 10))


# 从0-99这100个数中随机取出10个数，要求不能重复，可以自己设计数据结构。
# import random
#
# lst = []
#
# for _ in range(100):
#     item = int(random.random() * 100)
#     if item not in lst:
#         lst.append(item)
#     if len(lst) == 10:
#         break
#
# log(lst)


# 用Python实现 9*9 乘法表 （两种方式）
# for i in range(1, 10):
#     line = ''
#     for j in range(1, i+1):
#         line += f'{i}*{j} '
#     log(line)


# 请给出下面代码片段的输出并阐述涉及的python相关机制。

# def dict_updater(k, v, dic={}):
#     dic[k] = v
#     print(dic)
#
#
# dict_updater('one', 1)
# dict_updater('two', 2)
# dict_updater('three', 3, {})
"""
{'one': 1}
{'one': 1, 'two': 2}
{'three': 3}
"""


# 写一个装饰器出来。


# 用装饰器给一个方法增加打印的功能。


# as 请写出log实现(主要功能时打印函数名)
# import time
#
#
# def log1(f):
#     def inner(*args, **kwargs):
#         log(f'call {f.__name__}()')
#         v = f(*args, **kwargs)
#         log(time.strftime("%Y-%m-%d", time.localtime()))
#         return v
#     return inner
#
#
# @log1
# def now():
#     print("2013-12-25")
#
#
# now()

# 输出
# call now()
# 2013-12-25


# 向指定地址发送请求，将获取到的值写入到文件中。

# import requests # 需要先安装requests模块：pip install requests
#
# response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
# print(response.text)

# # 获取结构中的所有name字段，使用逗号链接起来，并写入到 catelog.txt 文件中。
# import json
#
# data = """[
#     {'id': 1, 'name': 'Python', 'hide': False, 'category': 1},
#     {'id': 2, 'name': 'Linux运维', 'hide': False, 'category': 4},
#     {'id': 4, 'name': 'Python进阶', 'hide': False, 'category': 1},
#     {'id': 7, 'name': '开发工具', 'hide': False, 'category': 1},
#     {'id': 9, 'name': 'Go语言', 'hide': False, 'category': 1},
#     {'id': 10, 'name': '机器学习', 'hide': False, 'category': 3},
#     {'id': 11, 'name': '技术生涯', 'hide': False, 'category': 1}
# ]"""


# 请列举经常访问的技术网站和博客


# 请列举最近在关注的技术


# 请列举你认为不错的技术书籍和最近在看的书（不限于技术）
