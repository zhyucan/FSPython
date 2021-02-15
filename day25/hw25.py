log = print


# 1.
# class Authentic:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def register(self):
#         log('注册成功')
#
#     def login(self):
#         log('登录成功')
#
#
# l = [('登录', 'login'), ('注册', 'register')]
# 循环这个列表
# 显示 序号 用户要做的操作
# 用户输入序号
# 你通过序号找到对应的login或者register方法
# 先实例化
# 调用对应的方法,完成登录或者注册功能

# def operator(name, age):
#     for i in range(len(l)):
#         log(f'{i} {l[i][0]}')
#
#     while 1:
#         num = input('输入序号: ').strip()
#         if num in ['0', '1']:
#             num = int(num)
#             op = l[num][1]
#
#             u = Authentic(name, age)
#             if op == 'login':
#                 u.login()
#             elif op == 'register':
#                 u.register()
#             break
#         else:
#             log('输入错误')
#
#
# operator('yucan', 123)


# 2.
# class User:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         log('吃啥')
#
#     def sleep(self):
#         log('碎了')

# 用户输入用户名密码性别
# 实例化对象
# 用户任意输入内容 : 不能用异常处理
# 如果输入的是属性名 打印属性值
# 如果输入的是方法名 调用fangfa
# 如果输入的什么都不是 不做操作

#
# name = input('name: ')
# password = input('password: ')
# sex = input('sex: ')
#
#
# def act(name, password, sex):
#     u = User(name, password, sex)
#     recv = input('说点啥: ').strip()
#     if recv in ['name', 'age', 'sex']:
#         log(u.__dict__[recv])
#     elif recv == 'eat':
#         u.eat()
#     else:
#         pass
#
#
# act(name, password, sex)


# 3.
# 注册之后,重启所有的用户丢失
# 一次执行的注册行为,在之后所有执行中都能够正常登录
# 两个登录程序和面向对象的内容整理在一起,两个都要明白,都要记住


# 4.
# 写一个自定义模块,里面有你自己实现的mypickle和myjson,
# 我只需要给你传递一个参数 'pickle'还是'json'
# import pickle
# import json
#
#
# class Mypickle:
#     def __init__(self, path):
#         self.file = path
#
#     def dump(self, obj):
#         with open(self.file, 'ab') as f:
#             pickle.dump(obj, f)
#
#     def load(self):
#         with open(self.file, 'rb') as f:
#             while True:
#                 try:
#                     yield pickle.load(f)
#                 except EOFError:
#                     break
#
#
# class Myjson:
#     def __init__(self, path):
#         self.file = path
#
#     def dump(self, obj):
#         with open(self.file, 'ab') as f:
#             st = json.dumps(obj)
#             f.write(st)
#
#     def load(self):
#         with open(self.file, 'rb') as f:
#             for i in f:
#                 yield json.loads(i)


# 5.
# 鸭子类型
# 实现 __len__ 方法
# class List:
#     def __init__(self):
#         self.l = []
#         self.length = 0
#
#     def append(self, e):
#         self.l.append(e)
#         self.length += 1
#
#     def __len__(self):
#         return self.length
#
#
# a = List()
# a.append(1)
# a.append(2)
# a.append(3)
# log(len(a))
# a.append(4)
# a.append(5)
# log(len(a))


# 6. 代码题(通过具体代码完成下列要求)：

# class A:
#     def func(self):
#         print('in A')
#
#
# class B:
#     def func(self):
#         print('in B')
#
#
# class C(A, B):
#     def func(self):
#         print('in C')
#
#
# c1 = C()
# c1.func()

# 可以改动上上面代码，完成下列需求：
# 对C类实例化一个对象产生一个c1，然后执行c1.func()

# 1. 让其执行C类中的func
# class A:
#     def func(self):
#         print('in A')
#
#
# class B:
#     def func(self):
#         print('in B')
#
#
# class C(A, B):
#     def func(self):
#         print('in C')
#
#
# c1 = C()
# c1.func()

# 2. 让其执行A类中的func
# class A:
#     def func(self):
#         print('in A')
#
#
# class B:
#     def func(self):
#         print('in B')
#
#
# class C(A, B):
#     pass
#
#
# c1 = C()
# c1.func()

# 3. 让其执行B类中的func
# class A:
#     pass
#
#
# class B:
#     def func(self):
#         print('in B')
#
#
# class C(A, B):
#     pass
#
#
# c1 = C()
# c1.func()

# 4. 让其既执行C类中的func，又执行A类中的func
# class A:
#     def func(self):
#         print('in A')
#
#
# class B:
#     def func(self):
#         print('in B')
#
#
# class C(A, B):
#     def func(self):
#         print('in C')
#         super().func()
#
#
# c1 = C()
# c1.func()

# 5. 让让其既执行C类中的func，又执行B类中的func
# class A:
#     pass
#
#
# class B:
#     def func(self):
#         print('in B')
#
#
# class C(A, B):
#     def func(self):
#         print('in C')
#         super().func()
#
#
# c1 = C()
# c1.func()


# 7. 下面代码执行结果是什么？为什么？
#
# class Parent:
#     def func(self):
#         print('in Parent func')
#
#     def __init__(self):
#         self.func()
#
#
# class Son(Parent):
#     def func(self):
#         print('in Son func')
#
#
# son1 = Son()
"""
in Son func
"""


# 8. p1.name，p2.name，A.name 分别是什么？
# p1.age，p2.age，A.age 分别又是什么？为什么？

# class A:
#     name = []
#
#
# p1 = A()
# p2 = A()
#
# p1.name.append(1)
# p1.age = 12
#
# log(p1.name, p2.name, A.name)
# log(p1.age, p2.age, A.age)
"""
[1] [1] [1]
12 error error
"""


# 9. 写出下列代码执行结果：
#
# class Base1:
#     def f1(self):
#         print('base1.f1')
#
#     def f2(self):
#         print('base1.f2')
#
#     def f3(self):
#         print('base1.f3')
#         self.f1()
#
#
# class Base2:
#     def f1(self):
#         print('base2.f1')
#
#
# class Foo(Base1, Base2):
#     def f0(self):
#         print('foo.f0')
#         self.f3()
#
#
# obj = Foo()
# obj.f0()
"""
foo.f0
base1.f3
base1.f1
"""


# 10. 看代码写结果：

# class Parent:
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
#
# Child2.x = 2
# print(Parent.x, Child1.x, Child2.x)
#
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)
"""
1 1 1
1 1 2
1 3 2
"""


# 11. 有如下类：
#
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A):
#     pass
#
# class E(B,C):
#     pass
#
# class F(C,D):
#     pass
#
# class G(D):
#     pass
#
# class H(E,F):
#     pass
#
# class I(F,G):
#     pass
#
# class K(H,I):
#     pass


# 如果这是经典类，请写出他的继承顺序。
#
# 如果这是新式类，请写出他的继承顺序，并写出具体过程。
# log(K.mro())
