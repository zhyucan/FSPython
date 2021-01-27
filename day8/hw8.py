log = print

# 1.有如下文件，a1.txt.txt，里面的内容为：
# 老男孩是最好的学校，
#
# 全心全意为学生服务，
#
# 只为学生未来，不为牟利。
#
# 我说的都是真的。哈哈
#
#
# ​	分别完成以下的功能：
#
# ​	a.将原文件全部读出来并打印。
# with open('a1.txt', encoding='utf-8', mode='r') as f:
#     log(f.read())

# ​	b,在原文件后面追加一行内容：信不信由你，反正我信了。
# with open('a1.txt', encoding='utf-8', mode='a') as f:
#     f.write('\n信不信由你，反正我信了。')

# ​	c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# with open('a1.txt', encoding='utf-8', mode='r+') as f:
#     log(f.read())
#     f.write('\n信不信由你，反正我信了。')

# ​	d,将原文件全部清空，换成下面的内容：
#
# ​	每天坚持一点，
#
# ​	每天努力一点，
#
# ​	每天多思考一点，
#
# ​	慢慢你会发现，
#
# ​	你的进步越来越大。
# with open('a1.txt', encoding='utf-8', mode='w') as f:
#     f.write('每天坚持一点，\r\n\r\n每天努力一点，\r\n\r\n每天多思考一点，\r\n\r\n慢慢你会发现，\r\n\r\n你的进步越来越大。')


# 2.有如下文件，t1.txt,里面的内容为：
#
# 葫芦娃，葫芦娃，
#
# 一根藤上七个瓜
#
# 风吹雨打，都不怕，
#
# 啦啦啦啦。
#
# 我可以算命，而且算的特别准:
#
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
#
# ​	分别完成下面的功能：
#
# ​	a,以r的模式打开原文件，利用for循环遍历文件句柄。
# with open('t1.txt', encoding='utf-8', mode='r') as f:
#     for line in f.readlines():
#         log(line.strip())

# ​	b,以r的模式打开原文件，以readlines()方法读取出来，
#   并循环遍历 readlines(),并分析a与b有什么区别？
#   深入理解文件句柄与 readlines()结果的区别。
# with open('t1.txt', encoding='utf-8', mode='r') as f:
#     l1 = f.readlines()
#     for l in l1:
#         log(l.strip())

# ​	c,以r模式读取‘葫芦娃，’前四个字符。
# with open('t1.txt', encoding='utf-8', mode='r') as f:
#     log(f.read(4))

# ​	d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# with open('t1.txt', encoding='utf-8', mode='r') as f:
#     log(f.readline().strip())

# ​	e,以a+ 模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。
# with open('t1.txt', encoding='utf-8', mode='a+') as f:
#     f.write('\r\n\r\n老男孩教育')
#     f.seek(0)
#     for line in f.readlines():
#         log(line.strip())


# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# apple 10 3
#
# tesla 100000 1
#
# mac 3000 2
#
# lenovo 30000 3
#
# chicken 10 3
#
# ​通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
# result = []
# with open('a.txt', encoding='utf-8', mode='r') as f:
#     for line in f.readlines():
#         if line != '\n':
#             dic = {}
#             a, b, c = line.split()
#
#             dic['name'] = a
#             dic['price'] = int(b)
#             dic['amount'] = int(c)
#         result.append(dic)
# log(result)


# 4.有如下文件：
# alex是老男孩python发起人，创建人。
#
# alex其实是人妖。
#
# 谁说alex是sb？
#
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
#
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
# import os
#
# with open('a4.txt', encoding='utf-8', mode='r') as f1,\
#         open('a4.bak', encoding='utf-8', mode='w') as f2:
#     for line in f1:
#         line = line.replace('alex', 'SB')
#         f2.write(line)
# os.remove('a4.txt')
# os.rename('a4.bak', 'a4.txt')


# 5.文件a5.txt内容(选做题)
# name:apple price:10 amount:3 year:2012
#
# name:tesla price:100000 amount:1 year:2013
#
# ​	通过代码，将其构建成这种数据类型：
#
# ​	[{'name':'apple','price':10,'amount':3,year:2012},
#
# ​	{'name':'tesla','price':1000000,'amount':1}......]
#
# ​	并计算出总价钱。
# result = []
# with open('a5.txt', encoding='utf-8', mode='r') as f:
#     for line in f.readlines():
#         if line != '\n':
#             dic = {}
#             for kv in line.split():
#                 k, v = kv.split(':')
#                 if v.isdecimal():
#                     dic[k] = int(v)
#                 else:
#                     dic[k] = v
#             result.append(dic)
# log(result)


# 6.文件a6.txt内容(选做题)
# 序号 部门 人数 平均年龄 备注
#
# 1 python 30 26 单身狗
#
# 2 Linux 26 30 没对象
#
# 3 运营部 20 24 女生多
#
# .......
#
# 通过代码，将其构建成这种数据类型：
#
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},...]
# result = []
# with open('a6.txt', encoding='utf-8', mode='r') as f:
#     for line in f.readlines():
#         if line != '\n':
#             dic = {}
#             a, b, c, d, e = line.split()
#
#             dic['序号'] = a
#             dic['部门'] = b
#             dic['人数'] = int(c)
#             dic['平均年龄'] = int(d)
#             dic['备注'] = e
#             result.append(dic)
# log(result)
