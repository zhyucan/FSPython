# Day2作业及默写
#
log = print
# 1. 判断下列逻辑语句的True,False.
#    1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# log(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# log(False or True or False and True and True or False)
# log(True)

#    2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# log(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# log(False and True or False and True and True or False)
# log(False)


# 2. 求出下列逻辑语句的值。
#    1),8 or 3 and 4 or 2 and 0 or 9 and 7
# log(8 or 3 and 4 or 2 and 0 or 9 and 7)
# log(8 or 4 or 0 or 7)
# log(8)

#    2),0 or 2 and 3 and 4 or 6 and 0 or 3
# log(0 or 2 and 3 and 4 or 6 and 0 or 3)
# log(0 or 4 or 0 or 3)
# log(4)


"""
# 3. 下列结果是什么？
#    1)、6 or 2 > 1
log(6 or 2 > 1)
log(6 or True)
log(6)

#    2)、3 or 2 > 1
log(3 or 2 > 1)
log(3 or True)
log(3)

#    3)、0 or 5 < 4
log(0 or 5 < 4)
log(0 or False)
log(False)

#    4)、5 < 4 or 3
log(5 < 4 or 3)
log(False or 3)
log(3)

#    5)、2 > 1 or 6
log(2 > 1 or 6)
log(True or 6)
log(True)

#    6)、3 and 2 > 1
log(3 and 2 > 1)
log(3 and True)
log(True)

#    7)、0 and 3 > 1
log(0 and 3 > 1)
log(0 and True)
log(0)

#    8)、2 > 1 and 3
log(2 > 1 and 3)
log(True and 3)
log(3)

#    9)、3 > 1 and 0
log(3 > 1 and 0)
log(True and 0)
log(0)

#    10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
log(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
log(True and 2 or True and 3 and 4 or True)
log(2 or 4 or True)
log(2)
"""


# 4. while循环语句基本结构？
# 5. 利用while语句写出猜大小的游戏：
#    设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
#    如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
"""
per_num = 66
while True:
    n = int(input('猜数字: '))
    if n > per_num:
        log('大了')
    elif n < per_num:
        log('小了')
    else:
        log('猜对了')
        break
"""


# 6. 在5题的基础上进行升级：
#    给用户三次猜测机会，如果三次之内猜测对了，
# 则显示猜测正确，退出循环，
# 如果三次之内没有猜测正确，
# 则自动退出循环，并显示‘太笨了你....’。
"""
per_num = 66
times = 3
while times > 0:
    n = int(input('猜数字: '))
    if n > per_num:
        log('大了')
    elif n < per_num:
        log('小了')
    else:
        log('猜对了')
        break
    times -= 1
if times == 0:
    log('太笨了你。。。')
"""


# 7. 使用while循环输出 1 2 3 4 5 6 8 9 10
# n = 1
# while n <= 10:
#     log(n)
#     n += 1


# 8. 求1-100的所有数的和
# n = 1
# result = 0
# while n <= 100:
#     result += n
#     n += 1
# log(result)


# 9. 输出 1-100 内的所有奇数
# n = 1
# while n <= 100:
#     if n % 2 == 1:
#         log(n)
#     n += 1

# 10. 输出 1-100 内的所有偶数
# n = 1
# while n <= 100:
#     if n % 2 == 0:
#         log(n)
#     n += 1


# 11. 求1-2+3-4+5 ... 99的所有数的和
# n = 1
# result = 0
# while n < 100:
#     if n % 2 == 0:
#         result -= n
#     else:
#         result += n
#     n += 1
# log(result)
int

# 12. 用户登录（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
# n = 3
# name = 'yucan'
# while n > 0:
#     user = input('输入用户名: ')
#     if user == name:
#         log('用户名正确')
#         break
#     else:
#         log('用户名不对, 你还有 {} 次机会'.format(n - 1))
#     n -= 1


# 13. 简述ASCII、Unicode、utf-8编码
"""
ASCII
英文 1 字节

Unicode
全部 4 字节

utf-8
英文 1 字节
中文 3 字节

gbk
英文 1 字节
中文 2 字节
"""


# 14. 简述位和字节的关系？
# 1 字节 == 8 位
# 1 byte == 8 bit
