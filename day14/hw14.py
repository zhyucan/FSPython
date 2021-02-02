log = print


# 1. 整理今天的笔记以及课上代码，完善昨天没有写完的作业，先把上午留的装饰器认证登录的完成。
#
# 2. 将课上模拟博客园登录的装饰器的认证的代码完善好，整清楚。
# login_status = {
#     'username': None,
#     'status': False,
# }
#
#
# def login():
#     with open('login', mode='r+', encoding='utf-8') as f:
#         user_dict = {}
#         for line in f:
#             k, v = line.strip().split('|')
#             user_dict[k] = v
#
#         index = 0
#         while index < 3:
#             name = input('名字: ')
#             password = input('密码: ')
#
#             if user_dict.get(name) != password:
#                 index += 1
#             else:
#                 return True
#         else:
#             return False
#
#
# def auth(func):
#     def inner():
#         if login_status['status']:
#             ret = func()
#             return ret
#
#         if login():
#             login_status['status'] = True
#             ret = func()
#             return ret
#         else:
#             log('登录失败')
#     return inner
#
#
# @auth
# def home():
#     print('欢迎访问博客园主页')
#
#
# home()


# 3. 看代码写结果：
# def wrapper(f):
#     def inner(*args, **kwargs):
#         print(111)
#         ret = f(*args, **kwargs)
#         print(222)
#         return ret
#     return inner
#
#
# @wrapper
# def func():
#     print(333)
#
#
# print(444)
# func()
# print(555)
"""
444
111
333
222
555
"""


# 4. 编写装饰器,在每次执行被装饰函数之前打印一句
# ’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。
# def wrapper(f):
#     def inner(*args, **kwargs):
#         log('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         ret = f(*args, **kwargs)
#         return ret
#     return inner


# 5. 为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# def wrapper(f):
#     def inner():
#         ret = f() + 100
#         return ret
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


# 6. 请实现一个装饰器，通过一次调用是函数重复执行5次。
# def wrapper(f):
#     def inner(*args, **kwargs):
#         for i in range(5):
#             f(*args, **kwargs)
#     return inner
#
#
# @wrapper
# def func(num):
#     log(num**2)
#
#
# func(10)


# 7. 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数
# 的时间节点写入文件中。函数名通过： 函数名.__name__获取
# import time
#
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))  # 当前时间节点
#
#
# def wrapper():
#     pass
#
#
# def func1(f):
#     print(f.__name__)
#
#
# func1(wrapper)
# import time
#
#
# def wrapper(f):
#     def inner(*args, **kwargs):
#         ret = f(*args, **kwargs)
#
#         name = f.__name__
#         struct_time = time.localtime()
#         t = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
#
#         with open('times', encoding='utf-8', mode='a') as f1:
#             f1.write(f'{t} {name}\n')
#
#         return ret
#     return inner
#
#
# @wrapper
# def func(num):
#     return num**2
#
#
# func(10)
# func(100)
# func(-5)
