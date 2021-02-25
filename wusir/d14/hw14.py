# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


"""
def wrapper(f):
    def inner(*args, **kwargs):
        v = f(*args, **kwargs)
        return v
    return inner
"""


# 1. 为函数写一个装饰器，在函数执行之后输入 after
# def wrapper(f):
#     def inner():
#         v = f()
#         log('after')
#         return v
#     return inner
#
#
# @wrapper
# def func():
#     print(123)
#
#
# func()


# 2. 为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# def wrapper(f):
#     def inner(*args, **kwargs):
#         v = f(*args, **kwargs)
#         return v + 100
#     return inner
#
#
# @wrapper
# def func():
#     return 7
#
#
# result = func()
# print(result)


# 3. 为函数写一个装饰器，根据参数不同做不同操作。
#
# flag为True，则 让原函数执行后返回值加100，并返回。
# flag为False，则 让原函数执行后返回值减100，并返回。
# def x(boo):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             v = f(*args, **kwargs)
#             if boo:
#                 return v + 100
#             else:
#                 return v - 100
#         return inner
#     return wrapper
#
#
# @x(True)
# def f1():
#     return 11
#
#
# @x(False)
# def f2():
#     return 22
#
#
# r1 = f1()
# log(r1)
# r2 = f2()
# log(r2)


# 4. 写一个脚本，接收两个参数。
#
# 第一个参数：文件
# 第二个参数：内容
# 请将第二个参数中的内容写入到 文件（第一个参数）中。
#
# # 执行脚本： python test.py oldboy.txt 你好
# import sys
#
# file, content = sys.argv[1:]
#
# with open(file, 'w') as f:
#     f.write(content)


# 5. 递归的最大次数是多少？
# 1000


# 6. 看代码写结果

# print("你\n好")
# print("你\\n好")
# print(r"你\n好")
"""
你
好
***
你\n好
***
你\n好
"""


# 7. 写函数实现，查看一个路径下所有的文件【所有】
# import os
#
#
# def check(file):
#     g = os.walk(file)
#     for a, b, c in g:
#         for i in c:
#             f = os.path.join(a, i)
#             log(f)
#
#
# check('oshw')


# 8. 写代码
# path = r"D:\code\test.pdf"
# 请根据path找到code目录下所有的文件【单层】，并打印出来。
# path = r"D:\code\test.pdf"
# c = path.split('\\')[1]
# check(c)


# 9. 写代码实现【题目1】和【题目2】
# def fib(lim):
#     fis, sec = 1, 2
#     index = 1
#     while sec < lim:
#         index += 1
#         fis, sec = sec, fis + sec
#     return index, fis
#
#
# log(fib(4000000))
# (32, 3524578)


# import copy
#
# dicta = {'a': 1, 'b': 2, 'c': '12e', 'd': 4, 'f': 'hello'}
# dictb = {'b': 3, 'd': 5, 'c': 'avc', 'm': 9, 'k': 'world'}
#
# dic = copy.deepcopy(dicta)
# for k, v in dictb.items():
#     if dic.get(k):
#         dic[k] = dic[k] + v
#     else:
#         dic[k] = v
#
# log(dic)


# 10. 看代码写结果
# def extendList(val, lst=[]):
#     lst.append(val)
#     return lst
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
# log(list1, list2, list3)
"""
[10, 'a']
[123]
[10, 'a']
"""


# 11. 实现如下面试题

# 1.
# ABC


# 2
# tupleA = ('a', 'b', 'c', 'd', 'e')
# tupleB = (1, 2, 3, 4, 5)
# res = {}
#
# log({tupleA[i]: tupleB[i] for i in range(5)})


# 3
# import sys
#
# sys.argv


# 4
# ip = "192.168.0.100"
# log(ip.split('.'))


# 5
# alist = ['a', 'b', 'c']
# log(','.join(alist))


# 6
# s = '1234A6FASKKSJJLSKWLM<SJKL90'
#
# log(s[-2:])
# log(s[1:3])


# 7
# alist = [1, 2, 3, 1, 3, 1, 2, 1, 3]
# log(alist[:3])


# 2
# def perfect(num):
#     product = 0
#     for i in range(num-1, 0, -1):
#         if num % i == 0:
#             product += i
#
#     return num == product
#
#
# lst = []
# for i in range(1000):
#     if perfect(i):
#         lst.append(i)
#
# log(lst)


# 3
# with open('a.txt') as f1, \
#         open('b.txt') as f2:
#     pass
