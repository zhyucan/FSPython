log = print


# 1.
# 猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
# 如果比66小，则显示猜测的结果小了;
# 只有等于66，显示猜测结果正确，然后退出循环。
# per = 66
# while 1:
#     num = input('num: ').strip()
#     if not num.isdecimal():
#         log('请输数字')
#         continue
#     num = int(num)
#     if num > per:
#         log('大了')
#     elif num < per:
#         log('小了')
#     else:
#         log('对了')
#         break


# 2.
# 在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，
# 如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’。
# per = 66
# count = 0
#
# while count < 3:
#     count += 1
#     num = input('num: ').strip()
#     if not num.isdecimal():
#         log('请输数字')
#         continue
#     num = int(num)
#     if num > per:
#         log('大了')
#     elif num < per:
#         log('小了')
#     else:
#         log('对了')
#         break
# else:
#     log('大笨蛋')


# 3.
# 使用两种方法实现输出
# 1
# 2
# 3
# 4
# 5
# 6
# 8
# 9
# 10
# for i in range(1, 11):
#     log(i)


# 4.
# 求1 - 100
# 的所有数的和
# s = 0
#
# for i in range(1, 101):
#     s += i
#
# log(s)


# 5.
# 输出
# 1 - 100
# 内的所有奇数
# s = 0
#
# for i in range(1, 101):
#     if i % 2 == 1:
#         s += i
#
# log(s)


# 6.
# 输出
# 1 - 100
# 内的所有偶数
# s = 0
#
# for i in range(1, 101):
#     if i % 2 != 1:
#         s += i
#
# log(s)


# 7.
# 求1 - 2 + 3 - 4 + 5...
# 99
# 的所有数的和
# s = 0
#
# for i in range(1, 99):
#     if i % 2 == 1:
#         s += i
#     else:
#         s -= i
#
# log(s)


# 8. ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
# name = 'yucan'
# pw = '123'
#
# index = 3
# while index > 0:
#     n = input('name: ')
#     p = input('password: ')
#     index -= 1
#     if n == name and p == pw:
#         log('correct')
#         break
#     else:
#         log(f'wrong, 还有{index}次机会')


# 9.
# 简述ASCII、Unicode、utf - 8
# 编码
"""
ascii
    英文: 1 字节
    中文: 不表示
unicode
    英文: 4 字节
    中文: 4 字节
utf-8
    英文: 1 字节
    中文: 3 字节
gbk
    英文: 1 字节
    中文: 2 字节
"""


# 10.
# 简述位和字节的关系？
# 1 byte = 8 bit


# 11.
# 猜年龄游戏
# 要求：允许用户最多尝试3次，
# 3 次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
# per = 66
# count = 0
#
# while count < 3:
#     count += 1
#     num = input('num: ').strip()
#     if not num.isdecimal():
#         log('请输数字')
#         continue
#     num = int(num)
#     if num > per:
#         log('大了')
#     elif num < per:
#         log('小了')
#     else:
#         log('恭喜')
#         break


# 12.
# 猜年龄游戏升级版
# 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，
# 如果回答Y，就继续让其猜3次，以此往复，
# 如果回答N，就退出程序，如何猜对了，就直接退出。
# per = 66
# count = 0
#
# while count < 3:
#     count += 1
#     num = input('num: ').strip()
#     num = int(num)
#     if num > per:
#         log('大了')
#     elif num < per:
#         log('小了')
#     else:
#         log('恭喜')
#         break
#
#     if count == 3:
#         log('还想继续玩吗, Y-想玩, N-不玩了')
#         yn = input('YorN: ').strip()
#         if yn == 'Y':
#             count = 0


# 13.
# 判断下列逻辑语句的True, False
# - 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
"""
True
"""


# not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# False


# 14.
# 求出下列逻辑语句的值。
# 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8


# 0 or 2 and 3 and 4 or 6 and 0 or 3
# 4


# 15.
# 下列结果是什么？
# log(6 or 2 > 1)
# log(3 or 2 > 1)
# log(0 or 5 < 4)
# log(5 < 4 or 3)
# log(2 > 1 or 6)
# log(3 and 2 > 1)
# log(0 and 3 > 1)
# log(2 > 1 and 3)
# log(3 > 1 and 0)
# log(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)

# 6
# 3
# False
# 3
# True
# True
# 0
# 3
# 0
# 2

