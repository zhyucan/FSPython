"""
login_status = {
    'username': None,
    'status': False,
}


def login():
    with open('login', mode='r+', encoding='utf-8') as f:
        user_dict = {}
        for line in f:
            k, v = line.strip().split('|')
            user_dict[k] = v

        index = 0
        while index < 3:
            name = input('名字: ')
            password = input('密码: ')

            if user_dict.get(name) != password:
                index += 1
            else:
                return True
        else:
            return False


def auth(func):
    def inner():
        if login_status['status']:
            ret = func()
            return ret

        if login():
            login_status['status'] = True
            ret = func()
            return ret
        else:
            log('登录失败')
    return inner


@auth
def home():
    print('欢迎访问博客园主页')


home()

20. 写一个函数完成三次登陆功能：

- 用户的用户名密码从一个文件register中取出。
- register文件包含多个用户名，密码，用户名密码通过|隔开，
  每个人的用户名密码占用文件中一行。
- 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
- 登陆成功返回True。
def login():
    with open('register', mode='r+', encoding='utf-8') as f:
        user_dict = {}
        for line in f:
            k, v = line.strip().split('|')
            user_dict[k] = v

        index = 0
        while index < 3:
            name = input('名字: ')
            password = input('密码: ')

            if user_dict.get(name) != password:
                index += 1
            else:
                log(True)
                break

        if index == 3:
            log(False)


login()


21. 再写一个函数完成注册功能：

- 用户输入用户名密码注册。
- 注册时要验证（文件regsiter中）用户名是否存在，
  如果存在则让其重新输入用户名，如果不存在，则注册成功。
- 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
- 注册成功后，返回True,否则返回False。
def register():
    with open('register', mode='r', encoding='utf-8') as f:
        user_dict = {}
        for line in f:
            k, v = line.strip().split('|')
            user_dict[k] = v

    index = 0
    while index < 3:
        name = input('名字: ')
        password = input('密码: ')

        if name in user_dict:
            index += 1
        else:
            with open('register', mode='a', encoding='utf-8') as f:
                f.write(f'\r\n{name}|{password}')
                log(True)
                break

    if index == 3:
        log(False)


register()

"""
