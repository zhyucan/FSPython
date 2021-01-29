#-*- coding = utf-8 -*-
#@Time : 2020/6/29 11:41
#@Author : straightup

# 1.简述解释型和编译型语言

# 2.变量命名的规范和建议

# 3.is和==的区别

# 4.简述位和字节的关系
# 一个字节等于8位

# 5.pass的作用
# 保持结构完整性，后续更改内容

# 6.简述break和continue的区别
# break直接跳出循环；continue结束本次循环，进入下一次

# 7.请书写三元运算的编写格式

# 8.用一行代码实现数据值的交换
# a=3,b=5,交换a,b的值

# 9.如何实现字符串的翻转？如：name='太白金星'翻转为'星金白太'
# name='太白金星'
# print(name[::-1])

# 10.列举布尔值为False的常见值？
# 0,'',[],{},(),set()

# 11.列举字符串、列表、字典的每个常用的5个方法
# str: upper(),replace(),isdecimal(),title(),切片,
# list: reverse(),count(),append(),insert(),pop(),remove()
# dict: update(),pop(),get(),fromkeys(),keys(),values(),items()

# 12.简述深浅copy

# 13.谈谈你对字符串的驻留机制的理解

# 14.列表l=[1,1,2,2,3,4,5,5,6,6,7,8]去重

# 15.写代码，将'1,2,3'变为['1','2','3']
# l1 = list('1,2,3'.split(','))
# print(l1)

# 16.写代码，将['1','2','3']变为'1,2,3'
# s1 = ','.join(['1','2','3'])
# print(s1)

# 17.在python3x版本中，s1='老男孩'，如何将s1转化为utf-8的bytes类型？转化成功后，得到s2，如何将s2转化为gbk的bytes类型？

# 18.
# li = list("abcde")
# # print(li[10])   # IndexError: list index out of range
# print(li[10:])    # []

# 19.考察深浅copy
# import copy
# a = [1,2,3,[4,5],6]
# b = a   # b和a完全共用
# c = copy.copy(a)
# # c是浅copy，外壳（列表）是自己的，里面的数据共用
# # 故a,b,c任何一个对[4,5]这个小列表改动，就都改动
# d = copy.deepcopy(a)
# # d是深copy，东西都是自己的
# b.append(10)
# c[3].append(11)
# d[3].append(12)
# print(a,b,c,d)   # [1,2,3,[4,5,11],6,10]  [1,2,3,[4,5,11],6,10]  [1,2,3,[4,5,11],6]  [1,2,3,[4,5,12],6]

# 20.考察循环列表时改变列表大小的后果
# 循环一个列表，实际上是按照索引循环的
# alist = [2,4,5,6,7]
# for var in alist:
#     if var % 2 == 0:
#         alist.remove(var)
# print(alist)   # [4,5,7]


#-*- coding = utf-8 -*-
#@Time : 2020/7/1 7:42
#@Author : straightup

# 机试题
# --------------------------------------------------------------------------------------
# 1.lis = [['哇',['how',{'good':['am',100,'99']},'太白金星'],'I']] （2分）
# # o列表lis中的'am'变成大写。(1分)
# # o列表中的100通过数字相加再转换成字符串的方式变成'10010'。(1分)
# lis = [['哇',['how',{'good':['am',100,'99']},'太白金星'],'I']]
#
# lis[0][1][1]['good'][0] = lis[0][1][1]['good'][0].upper()
# lis[0][1][1]['good'][1] = str(lis[0][1][1]['good'][1] + 9910)
# print(lis)

# --------------------------------------------------------------------------------------
# # 2.dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}} （3分）
# # o将'k3'对应的值的最后面添加一个元素'23'。(1分)
# # o将'k2'对应的值的第0个位置插入元素'a'。(1分)
# o将(1,2,3,)对应的值添加一个键值对'k4','v4'。(1分)
# dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}}
#
# dic[(1,2,3,)]['k3'].append('23')
# dic['k2'].insert(0,'a')
# dic[(1,2,3,)]['k4'] = 'v4'
#
# print(dic)

# --------------------------------------------------------------------------------------
# 3.实现一个整数加法计算器（多个数相加）：（5分）
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。

# def counter(arg):
#     count = 0
#     for i in arg:
#         i = int(i.strip())
#         count += i
#     return count
#
# content = input("请输入内容:").split('+')
# print(counter(content))

# --------------------------------------------------------------------------------------
# 4.请写一个电影投票程序。现在上映的电影列表如下：(10分)
# lst = ['复仇者联盟4', '驯龙高手3', '金瓶梅', '老男孩', '大话西游']
# 由用户给每一个电影投票.最终将该用户投票信息公布出来。
# 要求：
# o用户可以持续投票，用户输入序号，进行投票。比如输入序号 1，给金瓶梅投票1。
# o每次投票成功，显示给哪部电影投票成功。
# o退出投票程序后，要显示最终每个电影的投票数。
# 建议最终投票的结果为这种形式：
# {'金瓶梅': 0, '复仇者联盟4': 0, '驯龙高手3': , '老男孩': 0,'大话西游':0}
lst = ['复仇者联盟4', '驯龙高手3', '金瓶梅', '老男孩', '大话西游']
# 自己的答案：
# movie_list = {}
# for i in range(len(lst)):
#     movie_list[i+1] = lst[i]
# print(movie_list)
#
# vote_result = {}
# while 1:
#     you_vote = input('请输入要投票的电影序号(Q或q退出程序)：')
#     if you_vote.upper() == 'Q':
#         print(vote_result)
#         break
#     if movie_list[int(you_vote)] not in vote_result:
#         vote_result[movie_list[int(you_vote)]] = 1
#         print(f'成功给{movie_list[int(you_vote)]}投上一票！')
#     else:
#         vote_result[movie_list[int(you_vote)]] += 1
#         print(f'成功给{movie_list[int(you_vote)]}投上一票！')

# 老师的答案：
# dic = dict.fromkeys(lst,0)
# print(dic)  # {'复仇者联盟4': 0, '驯龙高手3': 0, '金瓶梅': 0, '老男孩': 0, '大话西游': 0}
#
# for index, movie_name in enumerate(lst, 1):
#     print(f'序号：{index} 电影名称：{movie_name}')
# dic = {}
# while 1:
#     num = input('请输入你要投票的电影序号：').strip()
#     if num.isdecimal():
#         num = int(num)
#         if 0 < num <= len(lst):
#             dic[lst[num-1]] = dic.get(lst[num-1],0) + 1  # 利用get()生成的返回值，创建字典或修改值！
#             # if lst[num-1] not in dic:
#             #     dic[lst[num-1]] = 1
#             # else:
#             #     dic[lst[num - 1]] += 1
#             print(f'成功给{lst[num-1]}投上一票！')
#         else:
#             print('不在范围内，请重新输入')
#     elif num.upper() == 'Q':break
#     else:
#         print('输入有误，重新输入')
#
# for movie_name,count in dic.items():
#     print(f'电影{movie_name}的最终得票数为{count}')

# --------------------------------------------------------------------------------------
# 5.有文件t1.txt里面的内容为:（10分）
# id,name,age,phone,job
# 1,alex,22,13651054608,IT 2,wusir,23,13304320533,Tearcher 3,taibai,18,1333235322,IT
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},......]

# with open('t1.txt',encoding='utf-8',mode='r') as f1:
#     msg_list = f1.readline().strip().split(',')  # ['id', 'name', 'age', 'phone', 'job']
#     per_list = f1.readline().strip().split(' ')  # ['1,alex,22,13651054608,IT', '2,wusir,23,13304320533,Tearcher', '3,taibai,18,1333235322,IT']
#     total_list = []
#     for item in per_list: # '1,alex,22,13651054608,IT'
#         per_msg = {}
#         for i in range(len(msg_list)):
#             per_msg[msg_list[i]] = item.split(',')[i]
#         total_list.append(per_msg)
#     print(total_list)

# --------------------------------------------------------------------------------------
# 6.按要求完成下列转化。(10分)
list3 = [
{"name": "alex", "hobby": "抽烟"},
{"name": "alex", "hobby": "喝酒"},
{"name": "alex", "hobby": "烫头"},
{"name": "alex", "hobby": "Massage"},
{"name": "wusir", "hobby": "喊麦"},
{"name": "wusir", "hobby": "街舞"},
{"name": "wusir", "hobby": "出差"},
{"name": "太白", "hobby": "洗脚"},
]
list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞","出差"]},
]
# 将list3 这种数据类型转化成list4类型,你写的代码必须支持可拓展.
# 比如list3 数据在加一个这样的字典{"name": "wusir", "hobby": "溜达"},
# list4 {"name": "wusir", "hobby_list": ["喊麦", "街舞", "溜达"]
# 或者list3增加一个字典{"name": "太白", "hobby": "开车"},
# list4{"name": "太白", "hobby_list": ["开车"],
# 无论按照要求加多少数据,你的代码都可以转化.如果不支持拓展,则4分,支持拓展则10分.

# 法1 直接构建
# l1 = []
# for i in list3:  # {"name": "alex", "hobby": "抽烟"}
#     for j in l1:
#         if i['name'] == j['name']:
#             j['hobby_list'].append(i['hobby'])
#             break
#     else:
#         l1.append({'name':i['name'],'hobby_list':[i['hobby']]})
# print(l1)
# 关键是这个 for-else 结构！

# 法2
# dic = {'alex':{"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
# 'wusir':{"name": "wusir", "hobby_list": ["喊麦", "街舞","出差"]}
# }
# # print(list(dic.values()))  # list4

# dic = {}
# for i in list3:
#     if i['name'] not in dic:
#         dic[i['name']] = {'name': i['name'],'hobby_list':[i['hobby'],]}
#     else:
#         dic[i['name']]['hobby_list'].append(i['hobby'])
# l1 = list(dic.values())
# print(l1)

# --------------------------------------------------------------------------------------

