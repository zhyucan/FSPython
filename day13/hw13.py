log = print

# 1. 看代码分析结果
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda: i)
#
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1,v2)
"""
9
9
"""


# 2. 看代码分析结果
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x+i)
#
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1, v2)
"""
11
10
"""


# 3. 看代码分析结果
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x:x+i)
#
# for i in range(0,len(func_list)):
#     result = func_list[i](i)
#     print(result)
"""
0 2...18
"""


# 4. 看代码写结果（面试题）：
# def func(name):
#     v = lambda x:x+name
#     return v
#
# v1 = func('太白')
# v2 = func('alex')
# v3 = v1('银角')
# v4 = v2('金角')
# print(v1,v2,v3,v4)
"""
<func obj>
<func obj>
银角太白
金角alex
"""


# 5. 看代码写结果【面试题】
# result = []
# for i in range(10):
#     func = lambda: i
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1,v2)
"""
9
[<func obj>,...]
9
9
"""


# 6. 看代码分析结果【面试题】
# def func(num):
#     def inner():
#         print(num)
#     return inner
#
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1,v2)
"""
9
[<func obj>, ...]
0
9
None, None
"""


# 7. 看代码写结果【新浪微博面试题】
# def func():
#     for num in range(10):
#         pass
#     v4 = [lambda: num+10,lambda: num+100,lambda: num+100,]
#     result1 = v4[1]()
#     result2 = v4[2]()
#     print(result1,result2)
# func()
"""
109
109
"""


# 8. 请编写一个函数实现将IP地址转换成一个整数。【面试题，较难,可以先做其他题】
# 如 10.3.9.12 转换规则为二进制：
#         10            00001010
#          3            00000011
#          9            00001001
#         12            00001100
# 再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
# def convert(ip):
#     lst = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]
#     return int(''.join(lst), 2)
#
#
# log(convert('10.3.9.12'))


# 9. 都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
# 1). 用map来处理字符串列表,把列表中所有人都变成sb,
# 比方alex_sb
# name = ['oldboy','alex','wusir']
# m = map(lambda x: x + '_sb', name)
# log(list(m))

# 2). 用map来处理下述l，然后用list得到一个新的列表，
# 列表中每个人的名字都是sb结尾
# l = [{'name':'alex'},{'name':'y'}]
# m = map(lambda x: {'name': x['name'] + '_sb'}, l)
# log(list(m))


# 10. 用filter来处理,得到股票价格大于20的股票名字
# shares={
#   'IBM':36.6,
#   'Lenovo':23.2,
#   'oldboy':21.2,
#   'ocean':10.2,
# }
# f = filter(lambda x: shares[x] > 20, shares)
# log(list(f))


# 11. 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中,
# 结果list一下[9110.0, 27161.0,......]
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#   {'name': 'FB', 'shares': 200, 'price': 21.09},
#   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#   {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# m = map(lambda x: x['shares'] * x['price'], portfolio)
# log(list(m))


# 12. 还是上面的字典，用filter过滤出单价大于100的股票。
# f = filter(lambda x: x['price'] > 100, portfolio)
# log(list(f))


# 13. 有下列三种数据类型，
# l1 = [1,2,3,4,5,6]
# l2 = ['oldboy','alex','wusir','太白','日天']
# tu = ('**','***','****','*******')
# ​写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
# [(3, 'wusir', ''), (4, '太白', '*******')]这样的数据。
# log(list(zip(l1[2:], l2[2:], tu[2:])))


# 14. 有如下数据类型(**实战题**)：
# l1 = [{'sales_volumn': 0},
#
#       {'sales_volumn': 108},
#
#       {'sales_volumn': 337},
#
#       {'sales_volumn': 475},
#
#       {'sales_volumn': 396},
#
#       {'sales_volumn': 172},
#
#       {'sales_volumn': 9},
#
#       {'sales_volumn': 58},
#
#       {'sales_volumn': 272},
#
#       {'sales_volumn': 456},
#
#       {'sales_volumn': 440},
#
#       {'sales_volumn': 239}]

# ​将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# log(list(sorted(l1, key=lambda x: x['sales_volumn'])))


# 15. 求结果(**面试题**)
# v = [lambda:x for x in range(10)]
#
# print(v)
#
# print(v[0])
#
# print(v[0]())
"""
[<func>, ...]
<func>
9
"""


# 16. 求结果(**面试题**)
# v = (lambda :x for x in range(10))
#
# print(v)
#
# print(v[0])
#
# print(v[0]())
#
# print(next(v))
#
# print(next(v)())
"""
<generator>
error
error
<func>
0
"""


# 17. map(str,[1,2,3,4,5,6,7,8,9])输出是什么? (**面试题**)
# map(str,[1,2,3,4,5,6,7,8,9])
# None


# 18. 求结果：（**面试题，比较难，先做其他题**）
# def num():
#     return [lambda x:i*x for i in range(4)]
#
#
# print([m(2) for m in num()])

"""
[6, 6, 6, 6]
"""


# 19. 有一个数组[3,4，1,2,5,6,6,5,4，3,3]请写一个函数，
# 找出该数组中没有重复的数的总和（上面数据的么有重复的总和为1+2=3)(面试题)
# lst = [3,4,1,2,5,6,6,5,4,3,3]
#
# s = filter(lambda x: lst.count(x) == 1, lst)
#
# log(sum(s))


# 20. 写一个函数完成三次登陆功能：
#
# - 用户的用户名密码从一个文件register中取出。
# - register文件包含多个用户名，密码，用户名密码通过|隔开，
#   每个人的用户名密码占用文件中一行。
# - 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# - 登陆成功返回True。
# def login():
#     with open('register', mode='r+', encoding='utf-8') as f:
#         user_dict = {}
#         for line in f:
#             k, v = line.strip().split('|')
#             user_dict[k] = v
#
#         index = 0
#         while index < 3:
#             name = input('名字: ')
#             password = input('密码: ')
#
#             if user_dict.get(name) != password:
#                 index += 1
#             else:
#                 log(True)
#                 break
#
#         if index == 3:
#             log(False)


# login()


# 21. 再写一个函数完成注册功能：
#
# - 用户输入用户名密码注册。
# - 注册时要验证（文件regsiter中）用户名是否存在，
#   如果存在则让其重新输入用户名，如果不存在，则注册成功。
# - 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# - 注册成功后，返回True,否则返回False。
# def register():
#     with open('register', mode='r', encoding='utf-8') as f:
#         user_dict = {}
#         for line in f:
#             k, v = line.strip().split('|')
#             user_dict[k] = v
#
#     index = 0
#     while index < 3:
#         name = input('名字: ')
#         password = input('密码: ')
#
#         if name in user_dict:
#             index += 1
#         else:
#             with open('register', mode='a', encoding='utf-8') as f:
#                 f.write(f'\r\n{name}|{password}')
#                 log(True)
#                 break
#
#     if index == 3:
#         log(False)
#
#
# register()


# 22. 用完成一个员工信息表的增删功能（选做题，有时间做，没时间周末做）。
#
# 文件存储格式如下：
#
# id,name,age,phone,job
#
# 1,Alex,22,13651054608,IT
#
# 2,太白,23,13304320533,Tearcher
#
# 3,nezha,25,1333235322,IT
#
# 现在要让你实现两个功能：
#
# 第一个功能是实现给文件增加数据，用户通过输入姓名，年龄，电话，工作，
# 给原文件增加数据（增加的数据默认追加到原数据最后一行的下一行），
# 但id要实现自增（id自增有些难度，id是不需要用户输入的但是必须按照顺序增加）。
# def add_data():
#     user_list = []
#
#     with open('msg', mode='r+', encoding='utf-8') as f:
#         for line in f:
#             if line != '\n' and line[0].isdecimal():
#                 id, name, age, phone, job = line.strip().split(',')
#
#                 user = dict()
#                 user['id'] = id
#                 user['name'] = name
#                 user['age'] = age
#                 user['phone'] = phone
#                 user['job'] = job
#
#                 user_list.append(user)
#
#     u = dict(
#         id='',
#         name=input('姓名: '),
#         age=input('年龄: '),
#         phone=input('电话: '),
#         job=input('工作: '),
#     )
#
#     with open('msg', mode='a', encoding='utf-8') as f:
#         u['id'] = str(int(user_list[-1]['id']) + 1)
#         f.write('\n\n{},{},{},{},{}'.format(u['id'], u['name'], u['age'], u['phone'], u['job']))
#
#
# add_data()


# 第二个功能是实现给原文件删除数据，用户只需输入id，则将原文件对应的这一条数据删除
# (删除后下面的id不变，比如此时你输入1，则将第一条数据删除，
#  但是下面所有数据的id值不变及太白，nezha的 id不变)
# import os
#
#
# def del_data():
#     user_list = []
#
#     with open('msg', mode='r+', encoding='utf-8') as f:
#         for line in f:
#             if line != '\n' and line[0].isdecimal():
#                 id, name, age, phone, job = line.strip().split(',')
#
#                 user = dict()
#                 user['id'] = id
#                 user['name'] = name
#                 user['age'] = age
#                 user['phone'] = phone
#                 user['job'] = job
#
#                 user_list.append(user)
#
#     del_id = input('id: ')
#
#     for i in user_list:
#         if i['id'] == del_id:
#             user_list.remove(i)
#
#     with open('msg.bak', mode='w') as f:
#         f.write('id,name,age,phone,job')
#
#         for i in user_list:
#             f.write('\n\n{},{},{},{},{}'.format(i['id'], i['name'], i['age'], i['phone'], i['job']))
#
#     os.remove('msg')
#     os.rename('msg.bak', 'msg')
#
#
# del_data()
