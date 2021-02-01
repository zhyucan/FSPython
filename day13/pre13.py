log = print


# def func(a, b):
#     return a + b
#
#
# log(func(3, 4))
#
#
# func1 = lambda a, b: a + b
#
#
# log(func1(3, 4))


# func = lambda a: (a[0], a[2])
#
# log(func('agdvs'))


# func = lambda a, b: max(a, b)
#
# log(func(3, 6))


# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]
#
# fil = filter(lambda e: e['age'] > 17, lst)
#
# log('__iter__' in dir(fil))
# log('__next__' in dir(fil))
#
# log(list(fil))


# lst = [1,2,3,4,5]
#
# m = map(str, lst)
#
# m1 = map(lambda i: str(i), lst)
#
# log(m, m1)
# log(list(m))
# log(list(m1))

# l1 = [1, 2, 3, 4, 5]
#
# l2 = [2, 4, 6, 8, 10]
#
# m = map(lambda a, b: a + b, l1, l2)
#
# log(list(m))


from functools import reduce


# def add(a, b):
#     return a + b
#
#
# l = [1, 2, 3, 4, 5]
#
# r = reduce(add, l)
#
# log(r)


# l = [1, 2, 3, 4, 5]
#
#
# def st(a, b):
#     return str(a) + str(b)
#
#
# r = reduce(st, l)
#
#
# log(r)


# def av():
#     series = []
#
#     def inner(new):
#         series.append(new)
#         total = sum(series)
#         return total / len(series)
#     return inner
#
#
# inn = av()
#
# log(inn(100)())
# log(inn(110)())
# log(inn(120)())


# def wrapper():
#     a = 1
#
#     def inner():
#         log(a)
#
#     return inner
#
#
# ret = wrapper()
# log(ret.__code__.co_freevars)


# a = 2
#
#
# def wrapper():
#     def inner():
#         print(a)
#     return inner
#
#
# ret = wrapper()
# log(ret.__code__.co_freevars)


# def wrapper(a, b):
#     def inner():
#         log(a)
#         log(b)
#     return inner
#
#
# a = 2
# b = 3
# ret = wrapper(a, b)
# log(ret.__code__.co_freevars)


# l2 = [('太白', 18), ('alex', 73), ('wusir', 35), ('口天', 41)]
#
#
# m = min(l2, key=lambda i: i[1])
#
# log(m)
