# !/usr/bin/env python
# -*- coding:utf-8 -*-

log = print


ip = '192.168.12.79'

ip_list = ip.split('.')

log(','.join([bin(int(i)).zfill(10) for i in ip_list]))
