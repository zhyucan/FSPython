# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print



# 程序设计：沙河商城
# 功能：
# 1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，
# 最后将用户名、密码、注册时间写入到文件。

# 2.用户登录，只有三次错误机会，一旦错误则冻结账户
# （下次启动也无法登录，提示：用户已经冻结）。

# 3.商品浏览，分页显示商品（小文件）
# 用户可以选择商品且可以选择数量然后加入购物车（在全局变量操作），
# 不再购买之后，需要讲购物车信息写入到文件，文件要写入到指定目录：
# shopping_car(文件夹)
#   - 用户名A(文件夹)
#       2019-11-11-09-59.txt
#       2019-11-12-11-56.txt
#       2019-12-11-11-47.txt
#   - 用户B(文件夹)
#       2019-11-11-11-11.txt
#       2019-11-12-11-15.txt
#       2019-12-11-11-22.txt
#   注意：重复购买同一件商品时，只更改购物车中的数量。

# 4.我的购物车，查看用户所有的购物车记录，
# 即：找到shopping_car目录下当前用户所有的购买信息，并显示：
# 2019-11-11-09-59
#   飞机|1000|10个
#   大炮|2000|3个
# 2019-11-12-11-56.txt
#   迫击炮|10000|10个
#   手枪|123|3个

# 5.用户未登录的情况下，如果访问 商品流程 、我的购物车 时，
# 提示登录之后才能访问，让用户先去选择登录（装饰器实现）。
import time
import json
import sys


class User:
    def __init__(self, name, password, time):
        self.name = name
        self.password = password
        self.time = time


def register():
    name = input('name: ').strip()
    password = input('password: ').strip()
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    with open('usg_msg', 'a') as f:
        u = User(name, password, t).__dict__
        u = json.dumps(u)
        f.write(f'{u}\n')


def state():
    with open('freeze') as f:
        return eval(f.read())


def change_state():
    with open('freeze', mode='w') as f:
        f.write('True')


def login():
    if state():
        log('用户已经冻结')
        sys.exit()
    index = 0
    while index < 3:
        name = input('name: ').strip()
        password = input('password: ').strip()
        if name == 'yucan' and password == '123':
            log('登录成功')
            break
        else:
            log('登录失败')
        index += 1
    else:
        change_state()
        log('用户已经冻结')


def skim():
    pass


def shopping():
    pass


def main():
    dic = {
        '1': register,
        '2': login,
        '3': skim,
        '4': shopping,
    }
    while 1:
        log("""沙河商城
        1 注册
        2 登录
        3 商品浏览
        4 我的购物车""")
        f = input('你要干嘛(N/n): ').strip()
        if f.upper() == 'N':
            return
        dic[f]()


if __name__ == '__main__':
    main()
