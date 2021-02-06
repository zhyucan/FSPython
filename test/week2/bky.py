log = print


def read_file(file_name):
    with open(file_name, mode='r+', encoding='utf-8') as f:
        user_dict = {}
        for line in f:
            k, v = line.strip().split('|')
            user_dict[k] = v

    return user_dict


def check_register(name, password):
    l = len(password)

    if l < 6 or l > 14:
        return False
    elif name in read_file('msg'):
        return False
    elif not name.isalnum():
        return False
    else:
        return True


def write_article(file_name, content):
    with open(file_name, mode='w+', encoding='utf-8') as f:
        for i in content:
            f.write(i)


def import_article(old_file, new_file):
    with open(old_file + '.md') as f1,\
            open(new_file + '.txt', encoding='utf-8', mode='w') as f2:
        content = f1.read()
        f2.write(content)


def login():
    with open('msg', mode='r+', encoding='utf-8') as f:
        user_dict = {}
        for line in f:
            k, v = line.strip().split('|')
            user_dict[k] = v

        index = 0
        while index < 3:
            name = input('名字: ')
            password = input('密码: ')

            if user_dict.get(name) != password:
                log('用户名或密码错误')
                index += 1
            else:
                return name, True
        else:
            return None, False


def register():
    with open('msg', mode='r', encoding='utf-8') as f:
        user_dict = {}
        for line in f:
            k, v = line.strip().split('|')
            user_dict[k] = v

    index = 0
    while index < 3:
        name = input('名字: ')
        password = input('密码: ')

        if check_register(name, password):
            log('注册成功')
            with open('msg', mode='a', encoding='utf-8') as f:
                f.write(f'\r\n{name}|{password}')
                return True
        else:
            log('注册失败')
            index += 1
    else:
        return False


def judge(f):
    def inner(u):
        if u['status']:
            ret = f(u)
            return ret

        name, status = login()
        if status:
            u['name'] = name
            u['status'] = True
            ret = f(u)
            return ret
        else:
            log('登录失败')
    return inner


@judge
def article(u):
    log(f'欢迎{u["name"]}进入文章页面')

    while 1:
        choice = input('直接写按 w, 导入文件按 d: ')

        c = choice.strip()
        if c == 'w':
            write_article('a', 'abc\n45')
            break
        elif c == 'd':
            import_article('abc', 'abc')
            break
        else:
            log('按要求输入哦')


@judge
def review(u):
    log(f'欢迎{u["name"]}进入评论页面')


@judge
def diary(u):
    log(f'欢迎{u["name"]}进入日记页面')


@judge
def fav(u):
    log(f'欢迎{u["name"]}进入收藏页面')


@judge
def cancel(u):
    u['status'] = False


def _quit():
    return exit()


def main(u):
    log("""
    1.请登录
    2.请注册
    3.进入文章页面
    4.进入评论页面
    5.进入日记页面
    6.进入收藏页面
    7.注销账号
    8.退出整个程序
    """)
    dic = {
        1: login,
        2: register,
        3: article,
        4: review,
        5: diary,
        6: fav,
        7: cancel,
        8: _quit,
    }
    while 1:
        choice = input('输入数字 1~8: ')
        if choice.isdecimal() and int(choice) in range(1, 9):
            num = int(choice)
            dic[num]()
        else:
            log('按要求输入数字喔~')


if __name__ == '__main__':
    user = {
        'name': None,
        'status': False,
    }
    
    main(user)
