# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


user_list = []

while 1:
    u = input('name: ')
    if u == 'N':
        log(user_list)
        break
    p = input('pwd: ')

    user = dict()
    user['name'] = u
    user['password'] = p
    user_list.append(user)


log('请登录')
u = input('name: ')
p = input('password: ')

for i in user_list:
    if i['name'] == u and i['password'] == p:
        log('登录成功')
        break
else:
    log('登录失败')
