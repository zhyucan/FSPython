log = print


# 请将列表中的每个元素通过 "_" 链接起来。
#
# users = ['李少奇', '李启航', '渣渣辉']
# 请将列表中的每个元素通过 "_" 链接起来。
# log('_'.join(users))


# 请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
# v2 = [44, 55, 66]
# v1 = (11, 22, 33)
# v2.extend(v1)
# log(v2)


# 请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素
# 追加到列表 v2 = [44,55,66] 中
# v2 = [44,55,66]
# v1 = (11,22,33,44,55,66,77,88,99)
# for i in range(len(v1)):
#     if i % 2 == 0:
#         v2.append(v1[i])
#
# log(v2)


# 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
#
# key_list = []
# value_list = []
# dic = dict({'a': 1, 'b': 2, 'c': 3,})
# for k, v in dic.items():
#     key_list.append(k)
#     value_list.append(v)
#
# log(key_list, value_list)


dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#
# a. 请循环输出所有的key
# for k in dic.keys():
#     log(k)

# b. 请循环输出所有的value
# for v in dic.values():
#     log(v)

# c. 请循环输出所有的key和value
# for k, v in dic.items():
#     log(k, v)

# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# log(dic)

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# log(dic)

# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic.get('k3').append(44)
# log(dic)

# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic.get('k3').insert(1, 18)
# log(dic)


av_catalog = {
    "欧美":{
        "www.太白.com": ["很多免费的,世界最大的","质量一般"],
        "www.alex.com": ["很多免费的,也很大","质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}
# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# av_catalog.get('欧美').get("www.太白.com").insert(2, '量很大')

# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog.get('欧美').get("hao222.com").pop(-1)

# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog.get('日韩').get("tokyo-hot")[-1] = av_catalog.get('日韩').get("tokyo-hot")[-1].upper()

# 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog.get('大陆')['1048'] = ['一天就封了']

# 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# av_catalog.get('欧美').pop("oldboy.com")

# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'

# av_catalog.get('大陆').get('1024')[0] = av_catalog.get('大陆').get('1024')[0] + '可以爬下来'
# log(av_catalog)


# 请循环打印k2对应的值中的每个元素。
#
# info = {
#     'k1':'v1',
#     'k2':[('alex'),('wupeiqi'),('oldboy')],
# }
# for i in info.get('k2'):
#     log(i)


# 有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
# s = "k: 1|k1:2|k2:3 |k3 :4"
# d = dict({})
# for i in s.split('|'):
#     k, v = i.split(':')
#     k, v = k.strip(), int(v)
#     d[k] = v
#
# log(d)


# 有如下值
# li = [11,22,33,44,55,66,77,88,99,90]
# 将所有大于 66 的值保存至字典的第一个key对应的列表中，
# 将小于 66 的值保存至第二个key对应的列表中。
# result = {'k1':[],'k2':[]}
# for i in li:
#     log(i)
#     if i > 66:
#         result.get('k1').append(i)
#     else:
#         result.get('k2').append(i)
#
# log(result)


# 输出商品列表，用户输入序号，显示用户选中的商品
#
# """
# 商品列表：
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       1 电脑 1999
#       2 鼠标 10
#       ...
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。
# """
# while True:
#     num = input('选择商品序号: ')
#
#     if num.lower() == 'q':
#         break
#
#     if num.isdecimal():
#         index = int(num) - 1
#         if 0 <= index <= len(goods) - 1:
#             good = goods[index]
#             name = good.get('name')
#             price = good.get('price')
#
#             log('{} {} {}'.format(index + 1, name, price))
#         else:
#             log('输入有误')
#     else:
#         log('输入有误')
