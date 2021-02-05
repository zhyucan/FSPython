# 1. 请实现一个装饰器，限制该函数被调用的频率，如10秒一次（借助于time模块，time.time()）（面试题,有点难度，可先做其他）

# 2. 请写出下列代码片段的输出结果：
# def say_hi(func):
#     def wrapper(*args,**kwargs):
#         print("HI")
#         ret=func(*args,**kwargs)
#         print("BYE")
#         return ret
#     return wrapper
#
# def say_yo(func):
#     def wrapper(*args,**kwargs):
#         print("Yo")
#         return func(*args,**kwargs)
#     return wrapper
# @say_hi
# @say_yo
# def func():
#     print("ROCK&ROLL")
# func()


# 5. 给l1 = [1,1,2,2,3,3,6,6,5,5,2,2] 去重，不能使用set集合（面试题）。

