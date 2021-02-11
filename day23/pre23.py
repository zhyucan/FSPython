log = print

# from math import pi
#
#
# class Circle(object):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * pow(self.radius, 2)
#
#     def circum(self):
#         return 2 * pi * self.radius
#
#
# class Ring(object):
#     def __init__(self, short, long):
#         self.small = Circle(short)
#         self.big = Circle(long)
#
#     def area(self):
#         short_area = self.small.area()
#         long_area = self.big.area()
#         return long_area - short_area
#
#     def circum(self):
#         short_circum = self.small.circum()
#         long_circum = self.big.circum()
#         return long_circum + short_circum
#
#
# r = Ring(5, 9)
# log(r.area())
# log(r.circum())


# class BirthDate(object):
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#
# class Course(object):
#     def __init__(self, name, price, period):
#         self.name = name
#         self.price = price
#         self.period = period
#
#
# class Teacher(object):
#     def __init__(self, name, gender, birth, course):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#         self.course = course
#
#     def teach(self):
#         log('teaching')


# p1=Teacher('egon','male',
#             BirthDate('1995','1','27'),
#             Course('python','28000','4 months')
#            )
#
# print(p1.birth.year,p1.birth.month,p1.birth.day)
#
# print(p1.course.name,p1.course.price,p1.course.period)

# Teacher.teach(2)

# class A(object):
#     count = 0
#
#     def __init__(self):
#         A.count += 1
#
#
# a = A()
# log(A.count)
#
# b = A()
# log(A.count)

class bjji(object):
    def __init__(self, cname, begint, teacher):
        self.cname = cname
        self.begint = begint
        self.teacher = teacher
        self.ke = keig


class keig(object):
    def __init__(self, name, cir, price):
        self.name = name
        self.cir = cir
        self.price = price


linux57 = bjji()
python22 = bjji()

log(linux57)
