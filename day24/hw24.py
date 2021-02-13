log = print


# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 登陆成功之后才创建用户对象
# 设计一个方法 修改密码
# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     def change_pw(self, new):
#         alter_pw(self.name, new)
#
#
# def user_list(file_name):
#     user_list = []
#
#     with open(file_name) as f:
#         for line in f:
#             user = {}
#             if line != '\n':
#                 k, v = line.strip().split('|')
#                 user[k] = v
#             user_list.append(user)
#
#     return user_list
#
#
# def login(name, password):
#         user_lst = user_list('msg')
#
#         for i in user_lst:
#             if (name, password) == list(i.items())[0]:
#                 return True
#         else:
#             return False
#
#
# def alter_pw(name, new_pw):
#     user_lst = user_list('msg')
#     for i in range(len(user_lst)):
#         dic = user_lst[i]
#         if dic.get(name):
#             user_lst[i][name] = new_pw
#
#     import os
#
#     with open('msg.bak', mode='w+') as f:
#         for i in user_lst:
#             k, v = list(i.items())[0]
#             f.write(f'{k}|{v}\n')
#
#     os.remove('msg')
#     os.rename('msg.bak', 'msg')
#
#
# def alter(name, password):
#     if login(name, password):
#         u = User(name, password)
#         while 1:
#             old = input('old: ')
#             new = input('new: ')
#
#             if old == password:
#                 u.change_pw(new)
#                 break
#             else:
#                 log('密码不对')
#     else:
#         log('登录失败')
#
#
# name = input('name: ')
# password = input('password: ')
#
# alter(name, password)


# 算法
# 二分查找  [1,2,3,4,5,6,7,8,9,10,27,36,46,58,69] - 有序列表
# in index 从列表中找到一个值的位置
# 实现上面的功能 - 用代码
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 36, 46, 58, 69]
#
#
# def index1(e, l, start=None, end=None):
#     n = len(lst)
#
#     return index1(e, l[start:end], start, end)
#
#
# log(index1(1, lst))
# log(index1(3, lst))
# log(index1(8, lst))
# log(index1(36, lst))
# log(index1(69, lst))


# sys.argv练习
# sys.argv 在执行python脚本的时候 写在python 之后的所有的内容,形成了一个列表
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python a.py alex sb cp \1.内容回顾.py \day21
# python a.py alex sb rm \6.作业.py
# python a.py alex sb rename \day23  \day24
# python a.py alex sb move \文件  \day24
# python a.py alex sb mkdir \新的文件夹名
# 在这个基础上实现一个move移动 把一个文件或者文件夹移动到另一个位置
# 创建文件夹
# import sys
# import os
#
#
# def ope():
#     lst = sys.argv
#     le = len(lst)
#     log(lst)
#
#     cp = lst[3]
#     if le == 5:
#         e = lst[4]
#         if cp == 'rm':
#             os.remove(e)
#         elif cp == 'mkdir':
#             os.mkdir(e)
#     elif le == 6:
#         e1, e2 = lst[4], lst[5]
#         if cp == 'rename':
#             os.rename(e1, e2)
#         elif cp == 'move':
#             pass
#
#
# ope()


# 练习 :
# 对象变成了一个属性
# 班级类
    # 包含一个属性 - 课程
# 课程
    # 课程名称
    # 周期
    # 价格

# 创建两个班级 linux57
# 创建两个班级 python22
# 查看linux57期的班级所学课程的价格
# 查看python22期的班级所学课程的周期
# class Cls:
#     def __init__(self, cs):
#         self.course = cs
#
#
# class Course:
#     def __init__(self, cname, cy, price):
#         self.cname = cname
#         self.cycle = cy
#         self.price = price
#
#
# li = Cls('linux57')
# py = Cls('python22')
#
# python = Course('linux57', 6, 200)
# linux = Course('python22', 5, 100)
#
# li.course = python
# log(li.course.price)
#
# py.course = linux
# log(py.course.cycle)


# #第一大题 : 读程序,标出程序的执行过程,画出内存图解,说明答案和为什么
# # 请不要想当然,执行之后检查结果然后再确认和自己的猜想是不是一致
# (1)
# class A:
#     Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的
#
#     def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#
#     def func1(self):
#         print(self)
#
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# A.Country = '英国'
# a.Country = '日本'
# print(a.Country)
# print(b.Country)
# print(A.Country)
"""
日本
英国
英国
"""


# (2)
# class A:
#     Country = ['中国']  # 静态变量/静态属性 存储在类的命名空间里的
#
#     def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#
#     def func1(self):
#         print(self)
#
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# a.Country[0] = '日本'
# print(a.Country)
# print(b.Country)
# print(A.Country)
"""
['日本']
['日本']
['日本']
"""


# (3)
# class A:
#     Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的
#
#     def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#         self.Country = country
#
#     def func1(self):
#         print(self)
#
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# A.Country = '英国'
# a.Country = '日本'
# print(a.Country)
# print(b.Country)
# print(A.Country)
"""
日本
泰国
英国
"""


# (4)
# class A:
#     Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的
#
#     def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
#         self.name = name
#         self.age = age
#
#     def Country(self):
#         return self.Country
#
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# print(a.Country)
# print(a.Country())
"""
<func>
印度
"""


