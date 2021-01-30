log = print


# # 笔试
# 1. 简述编译型和解释型语言。（1分）
#
# 2. 变量的命名规范和建议。（2分）
#
# 3. 简述 break 与 continue 的区别。（2分）
#
# 4. 简述 is 与 == 的区别。（1分）
#
# 5. 简述位和字节的关系。（1分）
#
# 6. 简述 pass 和 … 的作用。（1分）
#
# 7. 请书写三元运算的编写格式。（1分）
#
# 8. 看代码写运行结果：（1分）
# s = "{a},{b},{c}".format(a = "alex", b = "wusir", c = "太白")
# print(s)
"""
alex,wusir,太白
"""


# 9. 用一行代码实现数值的交换：（2分）
# a = [1,3]
# b = (5,6)
# 求 a,b 值一行互换
# a, b = b, a
# log(b, a)


# 10. 求出以下结果：（3分）
# print(9 or 1)
# print(1 and 2 or True)
# print(0 and 2 or 5 or 4)
"""
9
2
5
"""


# 11. 将字符串 name = "郭宝元" 反转。（2分）
# name = "郭宝元"
# log(name[::-1])


# 12. 列举 bool 值为 True 的常见值。（2分）


# 13. 列举字符串，列表，字典的每个常用方法各 5 种。（5分）


# 14. 简述深浅拷贝。（2分）


# 15. 在 python 3.X 中，将 s1 = "老男孩alex" 转换为 utf-8 的 byte 型，
# 转化成功后得到 s2，并将 s2 转化成 gbk 的 byte 型。（3分）
# s1 = "老男孩alex"
# s2 = s1.encode('utf-8')
# log(s2)
# s2 = s1.encode('gbk')
# log(s2)


# 16. "奇奇, 大象" 使用 utf-8 编码时，写出占位数与字节数，
# 使用 gbk 编码时，写出占位数与字节数。（2分）
# 14 10
# s = "奇奇, 大象"
# log(s.encode('utf-8'), s.encode('gbk'))


# 17. 看代码写结果：（2分）
# li = ["a","b","c","d","e"]
# print(li[6:10])
# []


# 18. 写代码将字符串 v = "k1,v1-k2,v2-k3,v3-…"
# 转换成字典 {"k1":"v1","k2":"v2","k3":"v3"…}（5分）
# v = "k1,v1-k2,v2-k3,v3"
# dic = {}
# for i in v.split('-'):
#     k, v = i.split(',')
#     dic[k] = v
#
# log(dic)


# 19. 看代码写结果：（2分）
# li = [1,2,3,4,5]
# print(li[4:2:-1])
# [5, 4]


# 20. 简述 intern 机制中数字与字符串的规则。（2分）


# 21. 将列表 li = [1,1,2,2,3,4,5,5,6,6,7,8] 去重。（2分）
# li = [1,1,2,2,3,4,5,5,6,6,7,8]
# li = list(set(li))
# log(li)


# 22. 写代码，将 "1_2_3" 转化为 ["1","2","3"]。（2分）
# log('1_2_3'.split('_'))


# 23. 写代码，将 ["1","2","3"] 变成 "1|2|3"。（2分）
# log('|'.join(["1","2","3"]))


# 24. 看代码写结果：（4分）
# import copy
# a = [1,2,3,[4,5],6]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# b.append(10)
# c[3].append(11)
# d[3].append(12)
# print(a,b,c,d)
"""
[1,2,3,[4,5,11],6,10]
[1,2,3,[4,5,11],6,10]
[1,2,3,[4,5,11],6]
[1,2,3,[4,5,12],6]
"""


# 25. 看代码写结果：（2分）
# name_list = ["周杰伦","马化腾","周星星","林俊杰","周园园","周扒皮"]
# for i in name_list:
#     if "周" in i:
#         name_list.remove(i)
#     log(i, name_list)
# print(name_list)
"""
["马化腾","林俊杰","周扒皮"]
"""


# 26. 现有字符串 a = "alexnb"，按需求写代码：（3分）
# a = "alexnb"
# 1. 获取 "exn" 三个字符。
# log(a[2:6])
# 2. 获取最后两个字符。
# log(a[-2:])
# 3. 获取 "bxl" 三个字符（顺序不变）。
# log(a[::-2])


# 27. 看代码写结果：（4分）
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# print(v2)
"""
[222,2,3,4,5]
[[222,2,3,4,5],[222,2,3,4,5],[222,2,3,4,5]]
"""


# 机试
# 1. lis = [['哇',['how',{'good':['am',100,'99']},'大帅哥'],'I']] （总分2分）
#    * 列表lis中的'am'全部变成大写。(1分)
#    * 列表中的100通过数字相加在转换成字符串的方式变成'10086'。(1分)
# lis = [['哇',['how',{'good':['am',100,'99']},'大帅哥'],'I']]
# lis[0][1][1]['good'][0] = lis[0][1][1]['good'][0].upper()
# log(lis)
# lis[0][1][1]['good'][1] = str(lis[0][1][1]['good'][1] + 9986)
# log(lis)


# 2. dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}}  （总3分）
#    * 将'k3'对应的值的最后面添加一个元素[1,2,3]。(1分)
#    * 将'k2'对应的值的第2个位置前插入元素{'a'}。(1分)
#    * 将(1,2,3,)对应的值添加一个键值对key:(1,)。(1分)
# dic = {
#     'k1': 'v1',
#     'k2': ['alex', 'sb'],
#     (1, 2, 3,): {'k3': ['2', 100, 'wer']}
# }
# dic[(1, 2, 3)]['k3'].append([1, 2, 3])
# dic['k2'].insert(2, {'a'})
# dic[(1, 2, 3)]['key'] = (1,)
# log(dic)


# 3. 实现一个整数加法计算器（多个数相加）：（5分）
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12    +  13，
# 去除所有的空白,然后进行分割再进行计算。
# def add1(content):
#     s = 0
#     for i in content.split('+'):
#         s += int(i)
#     return s
#
#
# content = input("请输入内容: ")
# log(add1(content))


# 4. 使用for循环计算1-3+5-7+9-11+13...99的结果(5分)
# s = 0
# index = 1
# for i in range(1, 100, 2):
#     s += i * index
#     index *= -1
#
# log(s)


# 5. 有文件t1.txt里面的内容为:（5分）
# 1,alex,22,13651054608,IT
# 2,wusir,23,13304320533,Tearcher
# 3,taibai,18,1333235322,IT
#
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},
#  {'id':'2','name':'wusir','age':'23','phone':'13304320533','job':'Tearcher'},
#  {'id':'3','name':'taibai','age':'18','phone':'1333235322','job':'IT'},]
# with open('t1.txt', encoding='utf-8') as f:
#     lst = []
#     for i in f:
#         line = {}
#         v1, v2, v3, v4, v5 = i.split(',')
#         line['id'] = v1
#         line['name'] = v2
#         line['age'] = v3
#         line['phone'] = v4
#         line['job'] = v5.strip()
#         lst.append(line)
#     log(lst)


# 6. 有如下车牌和车辆归属地,形成一个新的字典,显示每个归属地的车辆共有多少：(5分)
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪B25044','冀G11111']
# locals = {'冀':'河北', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京':'北京','沪':'上海'}
# 结果: {'⿊⻰江':2, '⼭东': 2, '北京': 1,'河北':1}
# result = {}
# for i in cars:
#     abbr = locals[i[0]]
#     if abbr in result:
#         result[abbr] += 1
#     else:
#         result[abbr] = 1
#
# log(result)


# 7. 有如下值li= ["a","b",11,22,33,44,55,"66","77","88","99"]，
# 将所有的数字保存至字典的第一个key中，将所有的字符串保存至第二个key的值中。(5分)
# li= ["a","b",11,22,33,44,55,"66","77","88","99"]
# dic = {'k1': [], 'k2': []}
# for i in li:
#     if type(i) == int:
#         dic['k1'].append(i)
#     elif type(i) == str:
#         dic['k2'].append(i)
#
# log(dic)


# 8. userinfo.txt 文件中存放以下结构:(总分10分)
# alex:alex3714
#
# wusir:123456
#
# meet:meet123
# 1. 让用户选择
# 2. 用户选择注册就将账号和密码添加到userinfo.txt中,
# 如果用户名存在就提示用户名存在,不存在就进行添加(3分)
# 3. 用户选择登录,就验证用户的账号和密码是否与userinfo.txt一致,
# 如果一致终止循环提示登录成功(3分)
# 4. 让用户登录三次,三次错误提示用户名已锁定,
# 并打印错误次数(使用字符串格式化)(4分)
# times = 0
# u = {'name': 'alex', 'password': 'alex371'}
#
# with open('test1/userinfo.txt', encoding='utf-8', mode='r+') as f:
#     user_all = []
#     for line in f:
#         user = {}
#         if line != '\n':
#             k, v = line.split(':')
#             user['name'] = k
#             user['password'] = v.strip()
#             user_all.append(user)
#
#     while times < 3:
#         choice = input('登录 or 注册: ')
#         if choice == '登录':
#             if u in user_all:
#                 log('登录成功')
#                 break
#             else:
#                 log(f'错误次数{times + 1}')
#         elif choice == '注册':
#             if u in user_all:
#                 log('用户名已存在')
#             else:
#                 f.write('\n\n{}:{}'.format(u['name'], u['password']))
#                 break
#         times += 1
#     if times == 3:
#         log('用户名已锁定')
