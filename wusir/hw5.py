# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 1.请将列表中的每个元素通过 "_" 链接起来。
# users = ['李少奇', '李启航', '渣渣辉']
# log('_'.join(users))

# 2。请将列表中的每个元素通过 "_" 链接起来。
# users = ['李少奇', '李启航', 666, '渣渣辉']
# log('_'.join([str(i) for i in users]))

# 3.请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
# v1 = (11,22,33)
# v2 = [44,55,66]
# v2.extend(v1)
# log(v2)

# 4.请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的
# 所有偶数索引位置的元素追加到列表 v2 = [44,55,66] 中。
# v1 = (11,22,33,44,55,66,77,88,99)
# v2 = [44,55,66]
# v2.extend((v1[i] for i in range(len(v1)) if i % 2 == 0))
# log(v2)

# 5.将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
# info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# key_list = []
# value_list = []
# key_list.extend(info.keys())
# value_list.extend(info.values())
# log(key_list)
# log(value_list)


# 6.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# a. 请循环输出所有的key
# for key in dic.keys():
#     log(key)

# b. 请循环输出所有的value
# for v in dic.values():
#     log(v)

# c. 请循环输出所有的key和value
# for k, v in dic.items():
#     log(k, v)

# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# log(dic)

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# log(dic)

# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# log(dic)

# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(1, 18)
# log(dic)

# 7.请循环打印k2对应的值中的每个元素。
# info = {
#     'k1': 'v1',
#     'k2': [('alex'), ('wupeiqi'), ('oldboy')],
# }
# for i in info['k2']:
#     log(i)

# 8.有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
# s = "k: 1|k1:2|k2:3 |k3 :4"
# lst = s.split('|')
# dic = {}
# for i in lst:
#     k, v = i.split(':')
#     k, v = k.strip(), int(v)
#     dic[k] = v
# log(dic)

# 9.写代码

"""
有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,
将所有大于 66 的值保存至字典的第一个key对应的列表中，
将小于 66 的值保存至第二个key对应的列表中。
"""
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# result = {'k1': [], 'k2': []}
# for i in li:
#     if i > 66:
#         result['k1'].append(i)
#     else:
#         result['k2'].append(i)
# log(result)


# 10.输出商品列表，用户输入序号，显示用户选中的商品

"""
商品列表：
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
      1 电脑 1999 
      2 鼠标 10
      ...
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
"""
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998}
# ]
#
# for i in range(len(goods)):
#     good = goods[i]['name']
#     price = goods[i]['price']
#     log(f'{i+1} {good} {price}')
#
# while 1:
#     user = input('num: ').strip()
#     if user.isdigit():
#         num = int(user)
#         if 1 <= num <= len(goods):
#             g = goods[num-1]
#             good = g['name']
#             price = g['price']
#             log(f'{good} {price}')
#             break
#         else:
#             log('输入有误，并重新输入')
#     elif user.upper() == 'Q':
#         break
#     else:
#         log('输入有误，并重新输入')
