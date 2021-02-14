log = print


# Queue队列 : 先进先出 FIFO(FIRST IN FIRST OUT)
# Stack栈   : 后进先出 LIFO(Last In First Out)
# 继承关系
# 完成代码的简化
class rlist:
    def __init__(self):
        self.lst = []

    def put(self, data):
        self.lst.append(data)
        log(self.lst)


class Queue(rlist):
    def get(self):
        self.lst.pop(0)
        log(self.lst)


class Stack(rlist):
    def get(self):
        self.lst.pop()
        log(self.lst)


# 自定义Pickle,借助pickle模块来完成简化的dump和load
    # pickle dump
        # 打开文件
        # 把数据dump到文件里
    # pickle load
        # 打开文件
        # 读数据

# 对象 = Mypickle('文件路径')
# 对象.load()  能拿到这个文件中所有的对象
# 对象.dump(要写入文件的对象)
import pickle


class Mypickle:
    def __init__(self, file):
        self.file = file

    def load(self):
        with open(self.file, 'rb') as f:
            while 1:
                try:
                    obj = pickle.load(f)
                    log(obj.__dict__)
                except EOFError:
                    break

    def dump(self, data):
        with open(self.file, 'ab') as f:
            pickle.dump(data, f)


# class Course:
#     def __init__(self, name, period, price):
#         self.name = name
#         self.period = period
#         self.price = price
#
#
# python = Course('python', '6 moneth', 21800)
# m = Mypickle('test_memo1')
# m.dump(python)
# m.load()
