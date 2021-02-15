class A:
    def __init__(self, name):
        self.name = name

    def f1(self):
        print('ag')


a = A('ds')
print(a.__dict__)
print(a.__dir__())
print(a.__class__)
