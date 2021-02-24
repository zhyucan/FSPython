# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 2. 请为 func 函数编写一个装饰器，添加上装饰器后可以实现：
# 执行func时，先输入"before"，然后再执行func函数内部代码。
# def wrapper(f):
#     def inner():
#         log('before')
#         return f()
#     return inner
#
#
# @wrapper
# def func():
#     return 100 + 200
#
#
# val = func()
# log(val)


# 3. 请为 func 函数编写一个装饰器，添加上装饰器后可以实现：
# 执行func时，先执行func函数内部代码，再输出 "after"
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
#     return 100 + 200
#
#
# val = func()
# log(val)


# 4. 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：
# 执行func时，先执行func函数内部代码，再输出 "after"
# def wrapper(f):
#     def inner(*args, **kwargs):
#         v = f(*args, **kwargs)
#         log('after')
#         return v
#     return inner
#
#
# @wrapper
# def func(a1):
#     return a1 + "傻叉"
#
#
# @wrapper
# def base(a1, a2):
#     return a1 + a2 + '傻缺'
#
#
# @wrapper
# def base1(a1, a2, a3, a4):
#     return a1 + a2 + a3 + a4 + '傻蛋'
#
#
# log(func('a'))
# log(base('a', 'b'))
# log(base1('a', 'b', 'c', 'd'))


# 5. 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：
# 将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。

# import random
#
#
# def wrapper(f):
#     def inner():
#         lst = []
#         for _ in range(5):
#             lst.append(f())
#         return lst
#     return inner
#
#
# @wrapper
# def func():
#     return random.randint(1, 4)
#
#
# result = func()
# print(result)


# 6. 请为以下函数编写一个装饰器，添加上装饰器后可以实现：
# 执行 read_userinfo 函时，先检查文件路径是否存在，
# 如果存在则执行，如果不存在则 输入文件路径不存在，
# 并且不再执行read_userinfo函数体中的内容，再讲 content 变量赋值给None。
# import os
#
#
# def wrapper(f):
#     def inner(path):
#         if os.path.exists(path):
#             return f(path)
#         else:
#             log('文件路径不存在')
#             return None
#     return inner
#
#
# @wrapper
# def read_userinfo(path):
#     file_obj = open(path, mode='r', encoding='utf-8')
#     data = file_obj.read()
#     file_obj.close()
#     return data
#
#
# content = read_userinfo('tes')
# log(content)


"""
温馨提示：如何查看一个路径是否存在？
import os
result = os.path.exists('路径地址')

result为True，则表示路径存在。
result为False，则表示路径不存在。
"""


# 7. 请为以下 user_lis t函数编写一个装饰器，校验用户是否已经登录，
# 登录后可以访问，未登录则提示：，请登录后再进行查看然后再给用户提示：
# 系统管理平台【1.查看用户列表】【2.登录】并选择序号。

# 此变量用于标记，用户是否经登录。
#    True,已登录。
#    False,未登录(默认)
def wrapper(f):
    def inner():
        if CURRENT_USER_STATUS:
            return f()
        else:
            log("请登录后再进行查看")
    return inner


CURRENT_USER_STATUS = False


@wrapper
def user_list():
    """查看用户列表"""
    for i in range(1, 10):
        temp = "ID:%s 用户名：老男孩-%s" % (i, i,)
        print(temp)


def login():
    """登录"""
    print('欢迎登录')
    while True:
        username = input('请输入用户名（输入N退出）：')
        if username == 'N':
            print('退出登录')
            return
        password = input('请输入密码：')
        if username == 'alex' and password == '123':
            global CURRENT_USER_STATUS
            CURRENT_USER_STATUS = True
            print('登录成功')
            return
        print('用户名或密码错误，请重新登录。')


def run():
    func_list = [user_list, login]
    while True:
        print("""系统管理平台
        1.查看用户列表；
        2.登录""")
        index = int(input('请选择：')) - 1
        if 0 <= index < len(func_list):
            func_list[index]()
        else:
            print('序号不存在，请重新选择。')


run()


# 8. 看代码写结果

# v = [lambda: x for x in range(10)]
# print(v)
# print(v[0])
# print(v[0]())
"""
[<lambda>, ..., <lambda>]
<lambda>
9
"""


# 9. 看代码写结果
#
# v = [i for i in range(10, 0, -1) if i > 5]
# log(v)
"""
[10, 9, 8, 7, 6]
"""


# 10. 看代码写结果
#
# data = [lambda x:x*i for i in range(10)]
# print(data)
# print(data[0](2))
# print(data[0](2) == data[8](2))
"""
[<lambda>,...,<lambda>]
18
True
"""


# 11. 请用列表推导式实现，踢出列表中的字符串，
# 然后再将每个数字加100，最终生成一个新的列表保存。
#
# data_list = [11, 22, 33, "alex", 455, 'eirc']
# new_data_list = [i for i in data_list if type(i) != str]
# log(new_data_list)


# 12. 请使用字典推导式实现，将如果列表构造成指定格式字典.

# data_list = [
#     (1, 'alex', 19),
#     (2, '老男', 84),
#     (3, '老女', 73)
# ]

# info_list = {
#     1:('alex',19),
#     2:('老男',84),
#     3:'老女',73)
# }

# log({i[0]: i[1:] for i in data_list})
