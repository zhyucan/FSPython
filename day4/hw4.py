log = print

# 1.写代码，有如下列表，按照要求实现每一个功能
#
# li = list(["alex", "WuSir", "ritian", "barry", "wenzhou"])
# 计算列表的长度并输出
# log(len(li))

# 列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# log(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(1, 'Tony')
# log(li)

# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = 'Kelly'
# log(li)

# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# log(li)

# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# li.extend(s)
# log(li)

# 请删除列表中的元素"ritian",并输出添加后的列表
# li.remove('ritian')
# log(li)

# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# log(li.pop(1))
# log(li)

# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# log(li)


# 2.写代码，有如下列表，利用切片实现每一个功能
#
li = [1, 3, 2, "a", 4, "b", 5, "c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# l1 = li[:3]
# log(l1)

# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# l2 = li[3:6]
# log(l2)

# 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# l3 = li[::2]
# log(l3)

# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# l4 = li[1:-1:2]
# log(l4)

# 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# l5 = li[-1:]
# log(l5)

# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# l6 = li[-3::-2]
# log(l6)

# 3.写代码，有如下列表，按照要求实现每一个功能。
#
# lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# log(lis)

# 将列表中的数字3变成字符串"100"（用两种方式）
# lis[3][2][1][1] = '100'
# log(lis)

# 将列表中的字符串"1"变成数字101（用两种方式）
# lis[3][2][1][2] = 101
# log(lis)


# 4.请用代码实现：
# li = ["alex", "wusir", "taibai", 2]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
# log('_'.join(li[:-1]))


# 5.利用for循环和range打印出下面列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in li:
#     log(i)
#
# for i in range(len(li)):
#     log(li[i])


# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# num_li = []
# for i in range(101):
#     if i % 2 == 0:
#         num_li.append(i)
# log(num_li)


# 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
# num_list = []
# for i in range(51):
#     if i % 3 == 0:
#         num_list.append(i)
# log(num_list)


# 8.利用for循环和range从100~1，倒序打印。
# for i in range(1, 101):
#     log(101 - i)


# 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
# num_list = []
# for i in range(100, 9, -1):
#     if i % 2 == 0:
#         num_list.append(i)
#
# log(num_list)
#
# for i in num_list:
#     if i % 4 != 0:
#         num_list.remove(i)
#
# log(num_list)


# 10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
# li = []
# for i in range(1, 31):
#     if i % 3 == 0:
#         li.append('*')
#     else:
#         li.append(i)
#
# log(li)


# 11.查找列表li中的元素，移除每个(for)元素的空格 strip，
# 并找出以"A"或者"a"开头startswith，并以"c"结尾的所有元素 endswith，
# 并添加到一个新列表new_l = []中,最后循环for 打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc", 'a c', 'adfdfdgdc']
# num_list = []
# for i in li:
#     if (i.startswith('A') or i.startswith('a')) and i.endswith('c'):
#         num_list.append(i)
#
# for i in num_list:
#     log(i)


# 12.开发敏感词语过滤程序，提示用户输入input评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# li1 = []
# comment = input('说点啥: ')
# n = 0
# for i in li:
#     if i in comment:
#         comment = comment.replace(i, '*' * len(i))
#     else:
#         n += 1
#
# if n == len(li):
#     li.append(comment)
# else:
#     li1.append(comment)
#
# log(li, li1)


# 13.有如下列表（选做题）
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7
# 8
# "taibai"
# 5
# ritian
# l1 = []
# for i in li:
#     if isinstance(i, list):
#         for j in i:
#             l1.append(j)
#     else:
#         l1.append(i)
#
# for i in range(len(l1)):
#     index = l1[i]
#     if isinstance(index, str):
#         l1[i] = index.lower()
#
# log(l1)
