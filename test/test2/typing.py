log = print
# 一. 代码题（20分）
#
# 1. 有列表
# a = ["7net", "www.7net", "www.septnet", "7net", "www"]
# 现需要从中将包含字符7net的元素给删掉，请以最少代码量实现。（3分）
# log([i for i in a if '7net' not in i])


# 2.
# l = ['班级20', '班级10', '班级3', '班级15', '班级32']
# 按照数字的顺序从小到大排序，不改变原列表，请以最少代码量实现。（3分）
# log(sorted(l, key=lambda x: int(x[2:])))


# 3. 现在有两元祖(('a'), ('b'))，(('c'), ('d'))，
# 请使用python中的匿名函数和内置函数生成列表[{'a': 'c'}, {'b': 'd'}] （3分）
# tup1 = ('a', 'b')
# tup2 = ('c', 'd')
# log([{i[0]: i[1]}for i in zip(tup1, tup2)])


# 4.
# alist = [{"a": 5, "b": 2}, {"a": 2, "b": 8}, {"a": 8, "b": 2}]
# 请写出以键a的值对alist进行排序的表达式（3分）
# log(sorted(alist, key=lambda x: x['a']))


# 5. 用filter函数过滤出单价大于100的股票。（3分）
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# log(list(filter(lambda x: x['price'] > 100, portfolio)))


# 6. 写一个生成器，里面的元素是20以内所有奇数的平方减一。(2分)
# gen = (i ** 2 - 1 for i in range(1, 21) if i % 2 == 1)
# log(type(gen), list(gen))


# 7. 求出l1列表中成绩最高的学生的姓名。（3分）
# l1 = [('张三', 59), ('李业', 67), ('小明', 99), ('小强', 47)]
# log(sorted(l1, key=lambda x: x[1])[-1][0])


# 二. 程序设计题。（40分）
# 用规范化项目目录的格式模拟一个ATM系统。

# 项目功能：
# 1. 登录（可支持多个账户（非同时）登录）。
# 2. 注册。
# 3. 查看余额。
# 4. 存钱。
# 5. 转账（给其他用户转钱）。
# 6. 查看账户流水。
# 7. 退出

# 提供的思路：
# ATM直译就是取款机，但是咱们是模拟一个取款机，
# 此取款机可以完成实现存钱，转账，查看余额，以及查看账户流水等功能。


# 要求以及分值分配：
# 1. 利用装饰器完成登录验证功能（3, 4, 5, 6功能需要验证）（5分）
# 2. 登录功能要求：用户名、密码（密码需要md5加密）从文件中读取，
# 进行三次验证，验证不成功则退出整个程序。（5分）
# 3. 注册功能要求：（5分）
# + 用户名要求：只能含有字母数字不能含有特殊字符并且要确保唯一性。
# + 密码的要求：长度在6与14个字符之间，密文存储。
# + 初始钱数：money: 0.
# + 注意：每个用户的以上信息通过字典以及json模块，以
# + 用户名.json的形式存储，用户的json文件存储在db文件夹中。
# 4. 查看余额功能要求：（5分）
# 用户登录成功之后，选择此功能即可显示账户余额，
# 并且将每次查看记录通过日志的方式记录到用户日志中（用户日志文件建议为：用户名.log）。
# 5. 存钱功能要求：（5分）
# 用户通过输入存储的钱数，然后将存储的钱累加到用户名.json那个json文件的字典中，
# 并且将每次存钱记录通过日志的方式记录到用户日志中（用户日志文件建议为：用户名.log）。
# 6. 转账功能要求：（5分）
# 用户通过输入对方用户名以及转账钱数完成给对方转账功能。
# + 要检测输入的对方用户账户是否存在。
# + 要检测你账户余额是否够用。
# + 将每次转账记录通过日志的方式记录到用户日志中（用户日志文件建议为：用户名.log）。
# 7.
# 查看流水要求：（5分）
# 用户通过选择此功能将用户专属的log打印出来。
# 8. 整个项目完成流畅，逻辑清楚，极少bug。（5分）
# 可能需要的模块：
"""
os模块：
# 和文件夹相关
os.makedirs('dirname1/dirname2')
可生成多层递归目录 ** *
os.removedirs('dirname1')
若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 ** *
os.mkdir('dirname')
生成单级目录；相当于shell中mkdir
dirname ** *
os.rmdir('dirname')
删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir
dirname ** *
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印 **
​
# 和文件相关
os.remove()
删除一个文件 ** *
os.rename("oldname", "newname")
重命名文件 / 目录 ** *
# path系列，和路径相关
os.path.abspath(path)
返回path规范化的绝对路径 ** *
os.path.split(path)
将path分割成目录和文件名二元组返回 ** *
os.path.dirname(path)
返回path的目录。其实就是os.path.split(path)
的第一个元素 **
os.path.basename(path)
返回path最后的文件名。如何path以／或\结尾，那么就会返回空值，即os.path.split(path)
的第二个元素。 **
os.path.exists(path)
如果path存在，返回True；如果path不存在，返回False ** *
os.path.isabs(path)
如果path是绝对路径，返回True **
os.path.isfile(path)
如果path是一个存在的文件，返回True。否则返回False ** *
os.path.isdir(path)
如果path是一个存在的目录，则返回True。否则返回False ** *
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ** *
os.path.getatime(path)
返回path所指向的文件或者目录的最后访问时间 **
os.path.getmtime(path)
返回path所指向的文件或者目录的最后修改时间 **
os.path.getsize(path)
返回path的大小 ** *

time模块：
time_now = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))

sys模块：
sys.path

hashlib模块：
import hashlib

md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())

json模块：
json.dumps()
json.loads()

logging模块
import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'all2.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态


if __name__ == '__main__':
    load_my_logging_cfg()
"""
