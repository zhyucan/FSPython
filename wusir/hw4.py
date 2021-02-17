# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 1.简述解释性语言和编译型语言的区别？


# 2.列举你了解的Python的数据类型？


# 3.写代码，有如下列表，按照要求实现每一个功能。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
# log(len(li))

# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
# log(li[::2])

# 列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# log(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(1, 'Tony')
# log(li)

# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[2] = 'Kelly'
# log(li)

# 请将列表的第3个位置的值改成 "太白"，并输出修改后的列表
# li[3] = '太白'
# log(li)

# 请将列表 l2=[1,"a",3,4,"heart"] 的每一个元素追加到列表li中，并输出添加后的列表
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# log(li)

# 请将字符串 s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# li.extend(s)
# log(li)

# 请删除列表中的元素"ritian",并输出添加后的列表
# li.remove('ritian')
# log(li)

# 请删除列表中的第2个元素，并输出删除元素后的列表
# li.pop(2)
# log(li)

# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
# li[2:5] = []
# log(li)


# 4.请用三种方法实现字符串反转 name = "小黑半夜三点在被窝玩愤怒的小鸟"（步长、while、for）
# name = "小黑半夜三点在被窝玩愤怒的小鸟"
# a1.
# log(name[::-1])
# a2.
# name1 = ''
# index = len(name) - 1
# while index >= 0:
#     name1 += name[index]
#     index -= 1
# log(name1)
# a3.
# name2 = ''
# for i in range(len(name)):
#     name2 += name[len(name) - i - 1]
# log(name2)


# 5.写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# 通过对li列表的切片形成新的列表 [1,3,2]
# log(li[:3])

# 通过对li列表的切片形成新的列表 ["a",4,"b"]
# log(li[3:-2])

# 通过对li列表的切片形成新的列表  [1,2,4,5]
# log(li[::2])

# 通过对li列表的切片形成新的列表 [3,"a","b"]
# log(li[1:-1:2])

# 通过对li列表的切片形成新的列表 [3,"a","b","c"]
# log(li[1::2])

# 通过对li列表的切片形成新的列表  ["c"]
# log(li[-1:])

# 通过对li列表的切片形成新的列表 ["b","a",3]
# log(li[-3::-2])


# 6.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# 0 武沛齐
# 1 景女神
# 2 肖大侠
# users = ["武沛齐","景女神","肖大侠"]
# for i in range(len(users)):
#     log(i, users[i])


# 7.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# 1 武沛齐
# 2 景女神
# 3 肖大侠
# users = ["武沛齐","景女神","肖大侠"]
# for i in range(len(users)):
#     log(i+1, users[i])


# 8.写代码，有如下列表，按照要求实现每一个功能。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"k"变成大写，并打印列表。
# lis[2] = lis[2].upper()
# log(lis)

# 将列表中的数字3变成字符串"100"
# lis[1] = '100'
# lis[3][2][1][1] = '100'
# log(lis)

# 将列表中的字符串"tt"变成数字 101
# lis[3][2][1][0] = 101
# log(lis)

# 在 "qwe"前面插入字符串："火车头"
# lis[3].insert(0, '火车头')
# log(lis)


# 9.写代码实现以下功能
# 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
# goods = ['汽车', '飞机', '火箭']
# for index, good in enumerate(goods):
#     log(index, good)

# 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
# while 1:
#     user = input('num: ').strip()
#     if user.isdecimal():
#         num = int(user)
#         if num in range(len(goods)):
#             log(f'您选择的商品是{goods[num]}')
#             break
#         else:
#             log('wrong')
#     else:
#         log('wrong')


# 10.请用代码实现,利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
# log('_'.join('alex'))


#  11.利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
# li = list()
# for i in range(0, 101, 2):
#     li.append(i)
# log(li)


# 12.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
# li = list()
# for i in range(0, 51):
#     if i % 3 == 0:
#         li.append(i)
# log(li)


# 13.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
# lst = ['a', 'b']
# for i in range(0, 51):
#     if i % 3 == 0:
#         lst.insert(0, i)
# log(lst)


# 14.查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，
# 并添加到一个新列表中,最后循环打印这个新列表。
# li = [' a', ' b ', 'dasa ', 'afds ', ' agsdf']
# l1 = []
# for i in li:
#     if i.strip().startswith('a'):
#         l1.append(i)
# for i in l1:
#     log(i)


# 15.判断是否可以实现，如果可以请写代码实现。
li = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry",), "wenzhou"]
# 请将 "WuSir" 修改成 "武沛齐"
# li[2] = "武沛齐"
# log(li)

# 请将 ("ritian", "barry",) 修改为 ['日天','日地']
# li[3] = ['日天','日地']
# log(li)

# 请将 88 修改为 87
# can't

# 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周"
# li.pop()
# li.insert(0, '文周')
# log(li)
