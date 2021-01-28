log = print

# 1.整理函数相关知识点,写博客。


# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def check(dic):
#     result = []
#     for i in enumerate(dic):
#         index, element = i
#         if index % 2 == 1:
#             result.append(element)
#     return result
#
#
# log(check([1, 2, 3, 4, 5]))


# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def len_greater_five(ele):
#     ele = eval(ele)
#     if len(ele) > 5:
#         return True
#     else:
#         return False
#
#
# e = input('说的啥: ')
# log(len_greater_five(e))


# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def dict_two(dic):
#     return dic[2:]
#
#
# log(dict_two([1, 2, 3]))


# 5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。
# def nums(s):
#     num, alpha, other = 0, 0, 0
#     for i in s:
#         if i.isdecimal():
#             num += 1
#         elif i.isalpha():
#             alpha += 1
#         else:
#             other += 1
#     return num, alpha, other
#
#
# log(nums('abc1234d&*%@#34'))


# 6.写函数，接收两个数字参数，返回比较大的那个数字。
# def check_num(a, b):
#     return a if a > b else b
#
#
# log(check_num(5, 4))


# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def check_dic(dic):
#     for k, v in dic.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#     return dic
#
#
# log(check_dic({'a': 'abcd', 'asd': '1235', 's': [2, 32, 'e', 32]}))


# # 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# # 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def list_to_dict(l):
#     dic = {}
#     for index, ele in enumerate(l):
#         dic[index] = ele
#     return dic
#
#
# log(list_to_dict([11, 22, 33]))


# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
# 用户通过输入这四个内容，然后将这四个内容传入到函数中，
# 此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def unit(name, sex, age, acade):
#     with open('student_msg.txt', 'w', encoding='utf-8') as f:
#         f.write('{} {} {} {}'.format(name, sex, age, acade))
#
#
# unit('yucan', 'man', 28, 'daxt')


# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。


# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
# import os
#
#
# def alter(filename, ori, con):
#     with open(filename, 'r', encoding='utf-8') as f1,\
#             open('a.bak', 'w', encoding='utf-8') as f2:
#         for line in f1:
#             line = line.replace(ori, con)
#             f2.write(line)
#     os.remove(filename)
#     os.rename('a.bak', filename)


# 5.写函数，在函数内部生成如下规则的列表 [1,1,2,3,5,8,13,21,34,55…]（斐波那契数列），并返回。
# 注意：函数可接收一个参数用于指定列表中元素最大不可以超过的范围。
# def fib(n):
#     if n == 1 or n == 0:
#         result = 1
#     else:
#         result = fib(n - 1) + fib(n - 2)
#     return result
#
#
# def fib_list(n):
#     l = []
#     index = 0
#     while True:
#         if fib(index) <= n:
#             l.append(fib(index))
#             index += 1
#         else:
#             break
#     return l
#
#
# log(fib_list(34))


# 6.写函数，验证用户名在文件 data.txt 中是否存在，如果存在则返回True，否则返回False。
# （函数有一个参数，用于接收用户输入的用户名）
# data.txt文件格式如下：
# 1|alex|123123
# 2|eric|rwerwe
# 3|wupeiqi|pppp
# def seek_name(name):
#     with open('data.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             if name in line:
#                 return True
#         return False
#
#
# log(seek_name('wupeiqi'))

