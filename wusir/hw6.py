# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 1.列举你了解的字典中的功能（字典独有）。
# get items keys values

# 2.列举你了解的集合中的功能（集合独有）。


# 3.列举你了解的可以转换为 布尔值且为False的值。
# '' 0 [] {} set() ()


# 4.请用代码实现
# info = {'name': '王刚蛋', 'hobby': '铁锤'}
# 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出
# （如果key不存在，则获取默认“键不存在”，并输出）。
# 注意：无需考虑循环终止（写死循环即可）
# while 1:
#     user = input('msg: ')
#     log(info.get(user, '键不存在'))


# 5.请用代码验证 "name" 是否在字典的键中？
# info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}
# info.get('name')


# 6.请用代码验证 "alex" 是否在字典的值中？
# info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}
# 'alex' in list(info.values())


# 7.有如下
# v1 = {'武沛齐', '李杰', '太白', '景女神'}
# v2 = {'李杰', '景女神'}
# 请得到 v1 和 v2 的交集并输出
# log(v1 & v2)

# 请得到 v1 和 v2 的并集并输出
# log(v1 | v2)

# 请得到 v1 和 v2 的 差集并输出
# log(v1 - v2)

# 请得到 v2 和 v1 的 差集并输出
# log(v2 - v1)


# 8.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
# lst = []
# while 1:
#     user = input('content: ')
#     if user.strip().upper() == 'N':
#         break
#     lst.append(user)
# log(lst)


# 9.循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
# lst = set()
# while 1:
#     user = input('content: ')
#     if user.strip().upper() == 'N':
#         break
#     lst.add(user)
# log(lst)


# 10.写代码实现
# v1 = {'alex', '武sir', '肖大'}
# v2 = []
# 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，
# 如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
# while 1:
#     user = input('name: ')
#     if user.upper() == 'N':
#         log(v1, v2)
#         break
#     if user in v1:
#         v2.append(user)
#     else:
#         v1.add(user)


# 11.判断以下值那个能做字典的key ？那个能做集合的元素？
# 1
# -1
# ""
# None
# [1, 2]
# (1,)
# {11, 22, 33, 4}
# {'name': 'wupeiq', 'age': 18}


# 12.is 和 == 的区别？
# is 内存地址
# == 值


# 13.type使用方式及作用？
# 判断类型


# 14.id的使用方式及作用？
# 内存地址


# 15.看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)
"""
True
False
"""


# 16.看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)
"""
True
True
"""


# 17.看代码写结果并解释原因
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# v1['k1'] = 'wupeiqi'
# print(v2)
"""
{'k1': 'wupeiqi', 'k2': [1, 2, 3]}
"""


# 18.看代码写结果并解释原因
# v1 = '人生苦短，我用Python'
# v2 = [1, 2, 3, 4, v1]
#
# v1 = "人生苦短，用毛线Python"
#
# print(v2)
"""
[1, 2, 3, 4, '人生苦短，我用Python']
"""


# 19.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
#
# info.append(9)
# print(userinfo)
#
# info = "题怎么这么多"
# print(userinfo)
"""
{'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
{'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
"""


# 20.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)
"""
['不仅多，还特么难呢', 2, 3]
[['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3]]
"""


# 21.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)
"""
['闭嘴', 2, 3]
[['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3]]
"""


# 22.看代码写结果并解释原因
# info = [1, 2, 3]
# user_list = []
# for item in range(10):
#     user_list.append(info)
#
# info[1] = "是谁说Python好学的？"
#
# print(user_list)
"""
[[1, "是谁说Python好学的？", 3],...,[1, "是谁说Python好学的？", 3]]
"""


# 23.看代码写结果并解释原因
# data = {}
# for item in range(10):
#     data['user'] = item
# print(data)
"""
{'user': 9}
"""


# 24.看代码写结果并解释原因
# data_list = []
# data = {}
# for item in range(10):
#     data['user'] = item
#     data_list.append(data)
# print(data_list)
"""
[{'user': 9},...,{'user': 9}]
"""


# 25.看代码写结果并解释原因
# data_list = []
# for item in range(10):
#     data = {}
#     data['user'] = item
#     data_list.append(data)
# print(data_list)
"""
[{'user': 0},...,{'user': 9}]
"""


# 使用循环打印出一下效果：
# *
# **
# ** *
# ** **
# ** ** *
# for i in range(1, 6):
#     n = i // 2
#     if i % 2 == 0:
#         log('** ' * n)
#     else:
#         log('** ' * n + '*')

# ** **
# ** *
# **
# *
# *
# ** *
# ** ** *
# ** ** ** *
# ** ** ** ** *
# for i in range(4, 0, -1):
#     n = i // 2
#     if i % 2 == 0:
#         log('** ' * n)
#     else:
#         log('** ' * n + '*')
#
# for i in range(1, 10, 2):
#     n = i // 2
#     if i % 2 == 0:
#         log('** ' * n)
#     else:
#         log('** ' * n + '*')


# 敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.
# 编程来完成敲七.给出⼀个任意的数字n.从1开始数.数到n结束.
# 把每个数字都放在列表中, 在数的过程中出现7
# 或者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个'咣'
#
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
# lst = []
# num = input('num: ')
# for i in range(1, int(num)+1):
#     if i % 7 == 0:
#         lst.append('咣')
#     else:
#         lst.append(i)
# log(lst)
