log = print

# 有了尾递归，编译器就可以更好的优化程序的执行过程

# 尾递归和循环一一对应

# 尾递归比线性递归多一个参数，这个参数是上一次调用函数得到的结果


# e.g.1
# x 的 y 次方

# 递归
def pow1(x, y):
    if y == 1:
        return x
    else:
        return pow1(x, y - 1) * x


# 循环
def pow2(x, y, result=1):
    while y > 0:
        result *= x
        y -= 1
    return result


# 尾递归
def pow3(x, y, result=1):
    if y == 0:
        return result
    else:
        return pow3(x, y - 1, result * x)


# e.g.2
# 阶乘

# 递归
def fac1(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fac1(n - 1)


# 循环
def fac2(n, result=1):
    while n >= 2:
        result *= n
        n -= 1
    return result


# 尾递归
def fac3(n, result=1):
    if n in [0, 1]:
        return result
    else:
        return fac3(n - 1, result * n)


# e.g.3
# 斐波那契数列

# 递归
def fib1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


# 循环
def fib2(n):
    fis, sec = 0, 1
    while n > 0:
        fis, sec = sec, fis + sec
        n -= 1
    return fis


# 尾递归
def fib3(n, fis=0, sec=1):
    if n == 1:
        return fis
    elif n == 2:
        return sec
    else:
        return fib3(n - 1, sec, fis+sec)
