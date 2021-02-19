# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 1.
# 看代码写结果
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
#
# v1.append(6)
# print(v1)
# print(v2)
"""
[1, 2, 3, 4, 5, 6]
[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
"""


# 2.
# 看代码写结果
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
#
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# print(v2)
"""
[222, 2, 3, 4, 5]
[[222, 2, 3, 4, 5], [222, 2, 3, 4, 5], [222, 2, 3, 4, 5]]
"""


# 3.
# 看代码写结果，并解释每一步的流程。
# v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v2 = {}
#
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item]
# print(v2)
"""
{'k1': [6, 7, 8, 9]}
"""


# 4.
# 简述深浅拷贝？


# 5.
# 看代码写结果
# import copy
#
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)
# print(v1 is v3)
"""
True
True
"""

# 6.
# 看代码写结果
# import copy
#
# v1 = [1, 2, 3, 4, 5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)
# print(v1 is v3)
"""
False
False
"""

# 7.
# 看代码写结果
# import copy
#
# v1 = [1, 2, 3, 4, 5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])
# print(v1[0] is v3[0])
# print(v2[0] is v3[0])
"""
True
True
True
"""

# 9.
# 看代码写结果
# import copy
#
# v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]
#
# v2 = copy.copy(v1)
#
# print(v1 is v2)
#
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
#
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
"""
False
True
True
True
True
True
"""

# 10.
# 看代码写结果
# import copy
#
# v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]
#
# v2 = copy.deepcopy(v1)
#
# print(v1 is v2)
#
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
#
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
"""
False

True
False

True
False
True
"""

# 11.
# 简述文件操作的打开模式


# 12.
# 请将info中的值使用 "_" 拼接起来并写入到文件"readme.txt"文件中。
# info = ['骗子，', '不是', '说', '只有', "10", '个题吗？']
# with open('readme.txt', 'w') as f:
#     f.write('_'.join(info))


# 14.
# 请将info中的所有键使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# 1. 请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# with open('readme.txt', 'a') as f:
#     f.write('_'.join(list(info.keys())))

# 2. 请将info中的所有值 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# with open('readme.txt', 'a') as f:
#     f.write('_'.join([str(i) for i in list(info.values())]))

# 3. 请将info中的所有键和值按照 "键|值,键|值,键|值" 拼接起来并写入到文件 "readme.txt" 文件中。
# with open('readme.txt', 'a') as f:
#     f.write(','.join([f'{str(k)}|{str(v)}' for k, v in list(info.items())]))


# 15.
# 写代码
# 要求：
# 如文件 data.txt  中有内容如下：
# wupeiqi|oldboy|wupeiqi@xx.com
# alex|oldboy|66s@xx.com
# xxxx|oldboy|yuy@xx.com
#
# 请用代码实现读入文件的内容，并构造成如下格式：
# info = [
#     {'name': 'wupeiqi', 'pwd': 'oldboy', 'email': 'wupeiqi@xx.com'},
#     {'name': 'alex', 'pwd': 'oldboy', 'email': '66s@xx.com'},
#     {'name': 'xxxx', 'pwd': 'oldboy', 'email': 'yuy@xx.com'},
# ]
# info = []
# with open('data.txt') as f:
#     for line in f:
#         user = {}
#         name, pwd, email = line.strip().split('|')
#         user['name'] = name
#         user['pwd'] = pwd
#         user['email'] = email
#         info.append(user)
# log(info)
