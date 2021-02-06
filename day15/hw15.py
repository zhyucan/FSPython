log = print


# 1. 请实现一个装饰器，限制该函数被调用的频率，如10秒一次
# （借助于time模块，time.time()）（面试题,有点难度，可先做其他）
# import time
#
#
# def wrapper(f):
#     def inner(*args, **kwargs):
#         ret = f()
#         log(time.time())
#         time.sleep(10)
#         return ret
#     return inner
#
#
# @wrapper
# def func(*args, **kwargs):
#     log('func')
#
#
# func()
# func()
# func()


# 2. 请写出下列代码片段的输出结果：
# def say_hi(func):
#     def wrapper(*args, **kwargs):
#         print("HI")
#         ret = func(*args, **kwargs)
#         print("BYE")
#         return ret
#
#     return wrapper
#
#
# def say_yo(func):
#     def wrapper(*args, **kwargs):
#         print("Yo")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @say_hi
# @say_yo
# def func():
#     print("ROCK&ROLL")
#
#
# func()
"""
hi
yo
ROCK&ROLL"
bye
"""


# 5. 给l1 = [1,1,2,2,3,3,6,6,5,5,2,2] 去重，不能使用set集合（面试题）。
# l1 = [1, 1, 2, 2, 3, 3, 6, 6, 5, 5, 2, 2]
#
#
# def func(lst):
#     l = []
#     for i in l1:
#         if i not in l:
#             l.append(i)
#     return l
#
#
# log(func(l1))
