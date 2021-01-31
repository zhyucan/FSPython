log = print


# def func():
#     yield 0
#     yield 1
#     yield 2
#     yield 4
#
#
# ret = func()
#
# log(next(ret))
# log(next(ret))
# log(next(ret))
# log(next(ret))


# def eat():
#     lst = []
#
#     for i in range(1, 10):
#         lst.append(i)
#
#     return lst
#
#
# log(eat())


# def eat1():
#     for i in range(1, 10):
#         yield i
#
#
# e = eat1()
#
# for i in range(5):
#     log(next(e))
#
# for i in range(3):
#     log(next(e))

# def func():
#     lst = [1, 2, 3, 4]
#     yield lst
#
#
# g = func()
#
# log(g, next(g))

# def func():
#     lst = [1, 2, 3, 4]
#     yield from lst
#
#
# g = func()
#
# log(next(g))
# log(next(g))
# log(next(g))

# def func():
#     lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
#     lst2 = ['馒头', '花卷', '豆包', '大饼']
#     yield from lst1
#     yield from lst2
#
#
# g = func()
# for i in g:
#     print(i)

# [i for i in range(10)]

# log([i**2 for i in range(1, 11)])

# log([i for i in range(101) if i % 2 == 0])

# log([f'python{i}期' for i in range(1, 101)])

# log([i for i in range(1, 31) if i % 3 == 0])

# lst = ['abc', 'a', 'agfgg', 'ad', '3et43rg']
# log([i.upper() for i in lst if len(i) >= 3])

# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# log([i for j in names for i in j if i.count('e') >= 2])

# gen = (i**2 for i in range(10))
#
# log(gen)
#
# for num in gen:
#     log(num)

# l1 = [1, 2, 3]
#
# l2 = ['a', 'b', 'c']
#
# log({l2[i]: l1[i] for i in range(0, 3)})

