import pickle

log = print


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price


python = Course('python', '6 moneth', 21800)
linux = Course('linux', '5 moneth', 19800)
go = Course('go', '4 moneth', 12800)

# with open('pp', 'ab') as f:
#     pickle.dump(linux, f)
#     pickle.dump(go, f)

with open('pp', 'rb') as f:
    while True:
        try:
            obj = pickle.load(f)
            log(obj.__dict__)
        except EOFError:
            break
