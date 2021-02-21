# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print

# 1.
# 将函数部分知识点，整理到自己笔记中。（搞明白课上讲的案例。）


# 2.
# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回。
def odd_item(ite):
    return list(ite[1::2])


# 3.
# 写函数，判断用户传入的一个对象（字符串或列表或元组任意）长度是否大于5，并返回真假。
def len_than_five(iter):
    return len(iter) > 5


# 4.
# 写函数，接收两个数字参数，返回比较大的那个数字。
def compare_num(a, b):
    return a if a > b else b


# 5.
# 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
# 用户通过输入这四个内容，然后将这四个内容传入到函数中，
# 此函数接收到这四个内容，将内容根据 "*"
# 拼接起来并追加到一个student_msg文件中。
def join_msg(name, sex, age, diploma):
    content = '*'.join([name, sex, age, diploma])
    with open('student_msg', 'w') as f:
        f.write(content)


# name = input('name: ')
# sex = input('sex: ')
# age = input('age: ')
# diploma = input('diploma: ')
#
# join_msg(name, sex, age, diploma)


# 6.
# 写函数，在函数内部生成如下规则的列表
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55…]（斐波那契数列），并返回。
# 注意：函数可接收一个参数用于指定列表中元素最大不可以超过的范围。
def fib_list(num):
    lst = []
    fir, sec = 1, 1
    while fir <= num:
        lst.append(fir)
        fir, sec = sec, fir + sec
    return lst


# log(fib_list(1))


# 7.
# 写函数，验证用户名在文件 data.txt 中是否存在，如果存在则返回True，
# 否则返回False。（函数有一个参数，用于接收用户输入的用户名）
#
# data.txt文件格式如下：
# 1 | alex | 123123
# 2 | eric | rwerwe
# 3 | wupeiqi | pppp
def exist_name(name):
    with open('data.txt') as f:
        for line in f:
            if name == line.split('|')[1].strip():
                return True
        else:
            return False


# while 1:
#     log(exist_name(input('name: ')))
