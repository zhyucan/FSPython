log = print

# 1. 定义一个类，计算圆的周长和面积。
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius**2
#
#     def circum(self):
#         return 2 * pi * self.radius


# c = Circle(3)
# log(c.area())
# log(c.circum())


# 2. 定义一个圆环类，计算圆环的周长和面积
# class Ring:
#     def __init__(self, inner, outer):
#         if inner < outer:
#             self.inner = Circle(inner)
#             self.outer = Circle(outer)
#         else:
#             self.inner = Circle(outer)
#             self.outer = Circle(inner)
#
#     def area(self):
#         return self.outer.area() - self.inner.area()
#
#     def circum(self):
#         return self.outer.circum() + self.inner.circum()
#
#
# r = Ring(6, 3)
# log(r.area())
# log(r.circum())


# 3.周末大作业：实现员工信息表
# 文件处理 + input
#
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
#
# 现在需要对这个员工信息文件进行增删改查。
#
# 不允许一次性将文件中的行都读入内存。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133
#
# 进阶选做：
# b.可创建新员工记录，id要顺序增加
# c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
#
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
# 其他需求尽量用函数实现
class Staff:
    def __init__(self, id, name, age, phone, job):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.job = job


def gene_staff(s):
    """
    :param s: 1,Alex,22,13651054608,IT
    :return: Staff()
    """
    id, name, age, phone, job = s.strip().split(',')
    return Staff(id, name, age, phone, job)


def split1(s, e):
    e1, e2 = s.split(e)
    return e1.strip(), e2.strip()


def ope(e, a, b):
    if e == '>':
        return a > b
    elif e == '<':
        return a < b
    elif e == '=':
        return a == b
    elif e == 'like':
        return b in a


def con(e, para, cond):
    if e in cond:
        e1, e2 = split1(cond, e)
        if para == '*':
            para = ['id', 'name', 'age', 'phone', 'job']
        else:
            para = para.split(',')
            para = [i.strip() for i in para]
        with open('user_msg') as f:
            for i in f:
                s = gene_staff(i).__dict__
                if ope(e, s[e1], e2):
                    pr = ''
                    for j in para:
                        pr += f'{s[j]},'
                    log(pr[:-1])


def seek():
    while 1:
        user = input('按文法查找: ')
        para, cond = split1(user[7:], 'where')
        if '>' in cond:
            con('>', para, cond)
        elif '<' in cond:
            con('<', para, cond)
        elif '=' in cond:
            con('=', para, cond)
        elif 'like' in cond:
            con('like', para, cond)


seek()
