# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 1.有变量name = "aleX leNb " 完成如下操作：
# name = "aleX leNb "
# 移除 name 变量对应的值两边的空格,并输出处理结果
# log(name.strip())

# 判断 name 变量是否以 "al" 开头,并输出结果（用切片）
# log(name[:2] == 'al')

# 判断name变量是否以"Nb"结尾,并输出结果（用切片）
# log(name[-2:] == 'Nb')

# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# log(name.replace('l', 'p'))

# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
# log(name.replace('l', 'p', 1))

# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果
# log(name.split('l'))

# 将name变量对应的值根据第一个"l"分割,并输出结果
# log(name.split('l', 1))

# 将 name 变量对应的值变大写,并输出结果
# log(name.upper())

# 将 name 变量对应的值变小写,并输出结果
# log(name.lower())

# 请输出 name 变量对应的值的第 2 个字符?
# log(name[1])

# 请输出 name 变量对应的值的前 3 个字符?
# log(name[:3])

# 请输出 name 变量对应的值的后 2 个字符?
# log(name[-2:])


# 2.有字符串
# s = "123a4b5c"
# 通过对s切片形成新的字符串 "123"
# log(s[:3])

# 通过对s切片形成新的字符串 "a4b"
# log(s[3:-2])

# 通过对s切片形成字符串s5,s5 = "c"
# s5 = s[-1]
# log(s5)

# 通过对s切片形成字符串s6,s6 = "ba2"
# s6 = s[-3::-2]
# log(s6)


# 3.使用while循环字符串 s="asdfer" 中每个元素。
# s = "asdfer"
# index = 0
# while 1:
#     index += 1
#     log(s[index-1])
#     if index == len(s):
#         break


# 4.使用while循环对s="321"进行循环，打印的内容依次是：
# "倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# index = 0
# while 1:
#     index += 1
#     log(f'倒计时{4-index}秒')
#     if index == 3:
#         log('出发')
#         break


# 5.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:")
# 用户输入：5+9或5+ 9或5 + 9（含空白），
# 然后进行分割转换最终进行整数的计算得到结果。
# content = input("请输入内容:")
# num1, num2 = [int(i) for i in content.split('+')]
# log(num1 + num2)


# 6.计算用户输入的内容中有几个 h 字符？
# 如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
# content = input("请输入内容：")
# count = 0
# for i in content:
#     if i == 'h':
#         count += 1
# log(count)


# 7.计算用户输入的内容中有几个 h 或 H 字符？
# 如：content = input("请输入内容：")   # 如fhdal234slfH9H769fjdla
# content = input("请输入内容：")
# count = 0
# for i in content:
#     if i.lower() == 'h':
#         count += 1
# log(count)


# 8.使用while循环分别正向和反向对字符串
# message = "伤情最是晚凉天，憔悴厮人不堪言。"
# index = 0
# while 1:
#     index += 1
#     log(message[index-1])
#     if index == len(message):
#         break
# index = 0
# while 1:
#     index += 1
#     log(message[len(message) - index])
#     if index == len(message):
#         break


# 9.获取用户输入的内容中 前4个字符中 有几个 A ？
# 如：content = input("请输入内容：")   # 如fAdal234slfH9H769fjdla
# content = input("请输入内容：")
# count = 0
# for i in content[:4]:
#     if i == 'A':
#         count += 1
# log(count)


# 10.如果判断name变量对应的值前四位"l"出现几次,并输出结果。


# 11.获取用户两次输入的内容，并将所有的数据获取并进行相加，如：
'''
要求：
将num1中的的所有数字倒找并拼接起来：1232312
将num2中的的所有数字倒找并拼接起来：1218323
然后将两个数字进行相加。
'''
