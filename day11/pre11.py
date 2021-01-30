log = print
#
# l1 = [1, 2, 3, 4, 5, 6]
#
# obj = iter(l1)
#
# while True:
#     try:
#         log(next(obj))
#     except StopIteration:
#         break


# def func(a, li=[]):
#     li.append(a)
#     return li


# log(func(10))
# # [10]
# log(func(20, []))
# # [20]
# log(func(100))
# # [20, 100]

# ret1 = func(10)
# ret2 = func(20, [])
# ret3 = func(100)
#
# log(ret1)
# # [10, 100]
# log(ret2)
# # [20]
# log(ret3)
# # [10, 100]


# def func():
#     global name
#     name = 'taibai'
#
#
# log(name)
# func()
# log(name)

# name = 'alex'
#
#
# def func():
#     global name
#     name = 'taibai'
#
#
# log(name)
# func()
# log(name)

# with open('aa', encoding='utf-8', mode='w') as f:
#     log('__iter__' in dir(f))
#     log('__next__' in dir(f))
