# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 列举你常见的内置函数。


# 列举你常见的内置模块？


# json序列化时，如何保留中文？
# import json
#
# s = 'vsgo 中国'
# data = json.dumps(s, ensure_ascii=False)
# log(data)


# 程序设计：用户管理系统
# 功能：
# 1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，最后将用户名、密码、注册时间写入到文件。
# 2.用户登录，只有三次错误机会，一旦错误则冻结账户（下次启动也无法登录，提示：用户已经冻结）。
# import time
# import json
#
#
# class User:
#     def __init__(self, name, password, time):
#         self.name = name
#         self.password = password
#         self.time = time
#
#
# def register():
#     name = input('name: ').strip()
#     password = input('password: ').strip()
#     t = time.strftime("%Y-%m-%d %H:%M:%S")
#     with open('usg_msg', 'a') as f:
#         u = User(name, password, t).__dict__
#         u = json.dumps(u)
#         f.write(f'{u}\n')


# register()

# import sys
#
#
# def state():
#     with open('freeze') as f:
#         return eval(f.read())
#
#
# def change_state():
#     with open('freeze', mode='w') as f:
#         f.write('True')
#
#
# def login():
#     if state():
#         log('用户已经冻结')
#         sys.exit()
#     index = 0
#     while index < 3:
#         name = input('name: ').strip()
#         password = input('password: ').strip()
#         if name == 'yucan' and password == '123':
#             log('登录成功')
#             break
#         else:
#             log('登录失败')
#         index += 1
#     else:
#         change_state()
#         log('用户已经冻结')
#
#
# login()


# 有如下文件，请通过分页的形式将数据展示出来。【文件非常小】
#
# 商品|价格
# 飞机|1000
# 大炮|2000
# 迫击炮|1000
# 手枪|123
# ...
# def glist(file):
#     lst = []
#
#     with open(file) as f:
#         for line in f:
#             line = line.strip()
#             lst.append(line)
#
#     return lst[1:]
#
#
# def display(page=1):
#     goods_list = glist('goods.txt')
#     goods_num = len(goods_list)
#
#     d, m = divmod(goods_num, page)
#
#     for i in range(page+1):
#         i *= d
#         log('*****************')
#         for j in goods_list[i:i+d]:
#             log(j)
#
#
# display(4)


# 有如下文件，请通过分页的形式将数据展示出来。【文件非常大】
#
# 商品|价格
# 飞机|1000
# 大炮|2000
# 迫击炮|1000
# 手枪|123
# ...
# def display(quantity):
#     with open('goods.txt') as f:
#         f.readline()
#         while 1:
#             for _ in range(quantity):
#                 line = f.readline().strip()
#                 if not line:
#                     return
#                 log(line)
#             log('******')


# display(4)


# 程序设计：购物车
# 有如下商品列表 GOODS_LIST，用户可以选择进行购买商品
# 并加入到购物车 SHOPPING_CAR 中且可以选择要购买数量，
# 购买完成之后将购买的所有商品写入到文件中【文件格式为：年_月_日.txt】
# 注意：重复购买同一件商品时，只更改购物车中的数量。

# # 购物车
# SHOPPING_CAR = {}
#
# # 商品列表
# GOODS_LIST = [
#     {'id': 1, 'title': '飞机', 'price': 1000},
#     {'id': 3, 'title': '大炮', 'price': 1000},
#     {'id': 8, 'title': '迫击炮', 'price': 1000},
#     {'id': 9, 'title': '手枪', 'price': 1000},
# ]
#
#
# import time
#
#
# def display(lst):
#     log('商品列表: ')
#     for i in range(len(lst)):
#         good = lst[i]
#         log('{} {} {}'.format(good['id'], good['title'], good['price']))
#
#
# def user_choice(id, num):
#     """
#     添加到购物车 SHOPPING_CAR
#     """
#     name = None
#     for i in GOODS_LIST:
#         if id == str(i['id']):
#             name = i['title']
#             break
#
#     if SHOPPING_CAR.get(name):
#         SHOPPING_CAR[name] = str(int(num) + int(SHOPPING_CAR[name]))
#     else:
#         SHOPPING_CAR[name] = num
#
#
# def write_car(dic):
#     """
#     把 SHOPPING_CAR 写入文件
#     :param dic: {'飞机': '2', '手枪': '8', '大炮': '88', }
#     :return: None
#     """
#     t = time.strftime("%Y_%m_%d")
#     filename = f'{t}.txt'
#     with open(filename, mode='w') as f:
#         for k, v in dic.items():
#             f.write(f'{k} {v} 件\n')
#
#
# def shopping():
#     display(GOODS_LIST)
#     while 1:
#         id = input('想要商品的序号(N/n): ').strip()
#         if id.upper() == 'N':
#             break
#         num = input('想要多少件: ').strip()
#         user_choice(id, num)
#     write_car(SHOPPING_CAR)


# shopping()
