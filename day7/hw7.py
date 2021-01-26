import copy


log = print

# day07 作业
#
# 看代码写结果
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
#
# v1.append(6)
# log(v1)
# log(v2)
# [1,2,3,4,5,6]
# [[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]]


# 看代码写结果
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
#
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# print(v2)
# [222,2,3,4,5]
# [[222,2,3,4,5], [222,2,3,4,5], [222,2,3,4,5]]


# 看代码写结果，并解释每一步的流程。
#
# v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item]
# print(v2)
# {'k1': [6, 7, 8, 9]}


# 简述深浅拷贝？
# 深浅拷贝对于不可变类型的数据无影响
# 对于可变类型，浅拷贝只能拷贝最外层，子元素是可变类型则未拷贝，子元素内存地址还是指向原来的地址
# 而深拷贝则会找到数据内部所有的可变类型进行拷贝


# 看代码写结果
#
# import copy
#
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)
# print(v1 is v3)
# False
# False


# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)
# print(v1 is v3)
# False
# False


# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,4,5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])
# print(v1[0] is v3[0])
# print(v2[0] is v3[0])
# TTT


# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[-1] is v2[-1])
# print(v1[-1] is v3[-1])
# print(v2[-1] is v3[-1])
# True False False


# 看代码写结果
#
# import copy
#
# v1 = [1, 2, 3, {'name': '太白', 'numbers': [7, 77, 88]}, 4, 5]
# v2 = copy.copy(v1)
#
# print(v1 is v2)
#
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
#
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
# TTTTTT


# 看代码写结果
#
# import copy
#
# v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
# v2 = copy.deepcopy(v1)
# print(v1 is v2)
#
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
#
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
# FTFFFT


# 请说出下面a,b,c三个变量的数据类型。
#
# ```python
# a = ('太白金星')
# b = (1,)
# c = ({'name': 'barry'})
# # ```
# log(type(a), type(b), type(c))
# str stuple, dict


# 按照需求为列表排序：
#
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# 从大到小排序
# 从小到大排序
# 反转l1列表
# l1.sort()
# log(l1)
# l1.sort(reverse=True)
# log(l1)
# l1.reverse()
# log(l1)


# 利用python代码构建一个这样的列表(升级题)：
# [['_','_','_'],['_','_','_'],['_','_','_']]
# result = []
# for i in range(3):
#     d = []
#     for j in range(3):
#         d.append('_')
#     result.append(d)
#
# log(result)


# 看代码写结果：
#
# l1 = [1,2,]
# l1 += [3,4]
# print(l1)
# [1, 2, 3, 4]


# 看代码写结果：
#
# ```python
# dic = dict.fromkeys('abc', [])
# dic['a'].append(666)
# dic['b'].append(111)
# print(dic)
# {'a': [666], 'b': [111], 'c': []}


# l1 = [11, 22, 33, 44, 55]
# 请把索引为奇数对应的元素删除
# del l1[::2]
# log(l1)


# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
# 请将字典中所有键带k元素的键值对删除.
# for k in list(dic.keys()):
#     if 'k' in k:
#         dic.pop(k)
#
# log(dic)


# bytes数据类型是python的基础数据类型，bytes类型存在的意义是什么？


# 列举bytes类型与str类型的三个不同点？


# 完成下列需求：
#
# s1 = '太白金星'
# 将s1转换成utf-8的bytes类型。
# log(s1.encode('utf-8'))
# 将s1转化成gbk的bytes类型。
# log(s1.encode('gbk'))


# b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
# b为utf-8的bytes类型，请转换成gbk的bytes类型。
# log(b.decode('utf-8').encode('gbk'))


# 用户输入一个数字，判断一个数是否是水仙花数。
# 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数.
# 那这个数就是一个水仙花数,
# 例如: 153 =1**3 + 5**3 + 3**3
# num = input('给个数: ')
# a, b, c = int(num[0]), int(num[1]), int(num[2])
# if int(num) == a**3 + b**3 + c**3:
#     log('是个水仙花')
# else:
#     log('不是吧')


# 把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# 结果: lst = ['麻花藤']
# log([i for i in lst if '周' not in i])


# 车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
# local = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京': '北京'}
# 结果: {'⿊⻰江':2, '⼭东': 1, '北京': 1}
# result = {}
#
# for k, v in local.items():
#     index = 0
#     for i in cars:
#         if k in i:
#             index += 1
#     result[v] = index
#
# log(result)
