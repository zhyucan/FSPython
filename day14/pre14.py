import time

log = print
#
#
# def check(func):
#     def inner(nn):
#         log(time.time())
#         ret = func(nn)
#         log(time.time())
#         return ret
#     return inner
#
#
# @check
# def index(nn):
#     log('欢迎访问')
#     return f'{nn}dfg'
#
#
# log(index('123'))
# check(index)('123')


user = {
    'name': None,
    'status': False,
}


def auth(f):
    def inner(*args, **kwargs):
        count = 0
        while count < 3:
            user['name'] = input('姓名: ')
            if user['name'] == 'yucan':
                user['status'] = True
                ret = f(*args, **kwargs)
                return ret
            else:
                count += 1
        else:
            log('登录失败')
    return inner


@auth
def diary():
    print('欢迎访问日记页面')


@auth
def comment():
    print('欢迎访问评论页面')


@auth
def home():
    print('欢迎访问博客园主页')


diary()
comment()
home()
