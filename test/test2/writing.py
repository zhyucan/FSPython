log = print

# 1. 简述 *args, **kwargs 的作用。（1分）


# 2. 看代码写结果：（5分）
# l = [1, 2, 3]
# d = {"a": 7, "b": 8}
#
#
# def f(arg1, arg2, *args, **kwargs):
#     print(arg1, arg2, args, kwargs)

# f(1, 2, 3, "groovy")
# 1 2 (3, 'groovy') {}

# f(arg1=1, arg2=2, c=3, zzz="h1")
# 1 2 () {'c': 3, 'zzz': 'h1'}

# f(1, 2, 3, a=1, b=2, c=3)
# 1 2 (3,) {'a': 1, 'b': 2, 'c': 3}

# f(*l, **d)
# 1 2 (3,) {"a": 7, "b": 8}

# f(1, 2, *l, q="winning", **d)
# 1 2 (1, 2, 3) {'q': 'winning', "a": 7, "b": 8}


# 3. 看代码写结果：（1分）
# for i in range(5,0,1):
#     print(i)
"""
None
"""


# 4. 看代码写结果：（3分）
# def f(x, l=[]):
#     for i in range(x):
#         l.append(i * i)
#     print(l)
#
#
# f(2)
# f(3, [3, 2, 1])
# f(3)
"""
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]
"""


# 5. 简述 python 的名称空间。（2分）


# 6. 执行下面的代码是否会报错？如果报错，请说出报错原因，并阐述解决办法。（2分）
# count = 1
# def func():
#     count += 1
# func()


# 7. 看代码写结果：（2分）
# def demo():
#     for i in range(3):
#         yield i
#
#
# g = demo()
#
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g1))
# print(list(g2))
"""
[0, 1, 2]
[]
"""


# 8. 简述 yield 于 yield from 的区别。（2分）


# 9. 看代码写结果。（2分）
# def func():
#     print("你好呀")
#     return "好你妹呀"
#
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)
"""
你好呀
好你妹呀
你好呀
好你妹呀
你好呀
好你妹呀
"""


# 10. 看代码写结果。（3分）
# def num():
#     return [lambda x:i*x for i in range(4)]
#
#
# print([m(2) for m in num()])
"""
[6, 6, 6, 6]
"""


# 11. 看代码写结果。（3分）
# v = (lambda: x for x in range(10))
#
# print(v)
# print(next(v))
# print(next(v)())
"""
<generator>
<function>
1
"""


# 12. 对于下列列表，请写一个函数，找出该数组中没有重复的数的总和。（3分）
# l = [2, 2, 1, 1, 4, 5, 3, 3, 6, 6]
#
#
# def sum1(lst):
#     return sum(set(lst))
#
#
# log(sum1(l))


# 13. 简述什么是闭包。（2分）


# 14. 实现一个装饰器，通过一次调用使函数重复执行 5 次。（3分）
# def wrapper(f):
#     def inner(*args, **kwargs):
#         for i in range(5):
#             f()
#     return inner


# 15. 写函数，遍历下列列表中的所有元素。（3分）
# l1 = [1, 2, 3, 4, [3, 4, 5, [11, 22, 33], 5, 6, 7]]
#
#
# def bl(lst):
#     for i in lst:
#         if isinstance(i, list):
#             bl(i)
#         else:
#             log(i)
#
#
# bl(l1)


# 16. 列举你曾使用过的至少 6 个 python 标准库。（2分）


# 17. 简述 sys.path.append() 作用。（2分）
