log = print


def foo(a, b, *args, c, sex=None, **kwargs):
    """
    a, b  位置参数
    *args 位置参数-动态
    c     默认参数-没有默认值
    sex   默认参数
    **kw  关键字参数
    """
    log(a, b)
    log(args)
    log(c)
    log(sex)
    log(kwargs)


# foo(1, 2, 3, 4, c=6)
# 1 2
# (3, 4)
# 6
# None
# {}

# foo(1, 2, sex='男', name='alex', hobby='old_woman')
# error

# foo(1, 2, 3, 4, name='alex', sex='男')
# error

# foo(1, 2, c=18)
# 1 2
# ()
# 18
# None
# {}

# foo(2, 3, [1, 2, 3], c=13, hobby='喝茶')
# 2 3
# ([1, 2, 3],)
# 13
# None
# {'hobby': '喝茶'}

# foo(*[1, 2, 3, 4], **{'name': '太白', 'c': 12, 'sex': '女'})
# 1 2
# (3, 4)
# 12
# 女
# {'name': '太白'}
