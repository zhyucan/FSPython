# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


# 慎用
def func(data, value=[]):
    pass


# 推荐
def func1(data, value=None):
    if not value:
        value = []
    pass


import time
for i in range(101):
    percent = '{}%\r'.format(i)
    time.sleep(0.1)
    log(percent, end='')
