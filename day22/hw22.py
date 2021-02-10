log = print


# 1. 完成下列功能:
#
#    1. 创建一个人类Person,再类中创建3个静态变量(静态字段)
#       animal = '高级动物'
#       soul = '有灵魂'
#       language = '语言'
#    2. 在类中定义三个方法,吃饭,睡觉,工作.
#    3. 在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄, 身高.
#    4. 实例化四个人类对象:
#       第一个人类对象p1属性为:中国,alex,未知,42,175.
#       第二个人类对象p2属性为:美国,武大,男,35,160.
#       第三个人类对象p3属性为:你自己定义.
#       第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3 的身高.
#    5. 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
#    6. 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
#    7. 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
#    8. 通过p1对象找到Person的静态变量 animal
#    9. 通过p2对象找到Person的静态变量 soul
#    10. 通过p3对象找到Person的静态变量 language
# class Person(object):
#     def __init__(self, country, name, sex, age, height):
#         self.animal = '高级动物'
#         self.soul = '有灵魂'
#         self.language = '语言'
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.height = height
#
#     def eat(self):
#         log(f'{self.name}在吃饭')
#
#     def sleep(self):
#         pass
#
#     def work(self):
#         pass
#
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# p2 = Person('美国', 'wusir', '男', 35, 160)
# p3 = Person('英国', 'yucan', 'man', 28, 172)
# p4 = Person(p1.country, p2.name, p3.sex, p2.age, p3.height)
#
# p1.eat()
# p2.eat()
# p3.eat()
# log(p1.animal)
# log(p2.soul)
# log(p3.language)


# 2. 通过自己创建类,实例化对象
#    在终端输出如下信息
#    小明，10岁，男，上山去砍柴
#    小明，10岁，男，开车去东北
#    小明，10岁，男，最爱大保健
#    老李，90岁，男，上山去砍柴
#    老李，90岁，男，开车去东北
#    老李，90岁，男，最爱大保健
#    老张…
# class Fav(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def act(self):
#         log(f'{self.name}，{self.age}岁，{self.sex}，上山去砍柴')
#         log(f'{self.name}，{self.age}岁，{self.sex}，开车去东北')
#         log(f'{self.name}，{self.age}岁，{self.sex}，最爱大保健')
#
#
# xm = Fav('小明', 10, '男')
# ll = Fav('老李', 90, '男')
# xm.act()
# ll.act()


# 3. 设计一个汽车类。
#
#    要求：
#
#    汽车的公共属性为：动力驱动，具有四个或以上车轮，主要用途载运人员或货物。
#    汽车的功能：run,transfer.
#
#    具体的汽车的不同属性：颜色，车牌，类型（越野，轿车，货车等）。
# class Bus(object):
#     def __init__(self, colour, plate, type):
#         self.colour = colour
#         self.plate = plate
#         self.type = type
#         self.use = '动力驱动，具有四个或以上车轮，主要用途载运人员或货物。'
#
#     def run(self):
#         pass
#
#     def transfer(self):
#         pass


# 4. 模拟英雄联盟写一个游戏人物的类（升级题）.
#    要求:
#    1. 创建一个 Game_role的类.
#    2. 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#    3. 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#       例: 实例化一个对象 盖伦,ad为10, hp为100
#       实例化另个一个对象 剑豪 ad为20, hp为80
#       盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血, 还剩多少血'的提示功能.
# class GameRole(object):
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self, figure):
#         hp1 = figure.ad
#         hp2 = self.hp - hp1
#         log(f'{self.name}攻击{figure.name},{self.name}掉了{hp1}血, 还剩{hp2}血')
#
#
# gl = GameRole('盖伦', 10, 100)
# jh = GameRole('剑豪', 20, 80)
# gl.attack(jh)


# 1. 暴力摩托程序（完成下列需求）：
#
#    1. 创建三个游戏人物，分别是：
#
#       ​	苍井井，女，18，攻击力ad为20，血量200
#
#       ​	东尼木木，男，20，攻击力ad为30，血量150
#
#       ​	波多多，女，19，攻击力ad为50，血量80
#
#    2. 创建三个游戏武器，分别是：
#
#       1. 平底锅，ad为20
#       2. 斧子，ad为50
#       3. 双节棍，ad为65
#
#    3. 创建三个游戏摩托车，分别是：
#
#       1. 小踏板，速度60迈
#       2. 雅马哈，速度80迈
#       3. 宝马，速度120迈
#
#  完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：
#
# ​	（1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
#
# ​	（2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
#
# ​	（3）波多多骑着雅马哈开着80迈的车行驶在赛道上。
#
# ​	（4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
#
# ​	（5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。
#
# ​	（6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
#
# ​	（7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
#
# ​	（8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。（选做）
#
# ​	（9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。（选做）
# class Npc(object):
#     def __init__(self, name, sex, age, ad, hp):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.ad = ad
#         self.hp = hp
#
#     def drive(self, moto):
#         log(f'{self.name}骑着{moto.name}开着{moto.speed}迈的车行驶在赛道上。')
#
#     def ko1(self, np):
#         hp1 = self.ad
#         hp2 = np.hp - hp1
#         log(f'{self.name}赤手空拳打了{np.name}{hp1}滴血，{np.name}还剩{hp2}血。')
#
#     def ko2(self, np, wea):
#         hp = np.hp - self.ad - wea.ad
#         log(f'{self.name}利用{wea.name}打了{np.name}一{wea.name}，{np.name}还剩{hp}血。')
#
#     def ko3(self, np, moto1, moto2, wea):
#         hp = np.hp - self.ad - wea.ad
#         log(f'{self.name}骑着{moto1.name}打了骑着{moto2.name}的{np.name}一{wea.name}，{np.name}哭了，还剩{hp}血。')
#
#
# class Weapon(object):
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#
# class Moto(object):
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#
# cjk = Npc('苍井空', '女', 18, 20, 200)
# dsn = Npc('动你', '男', 20, 30, 150)
# bod = Npc('波多', '女', 19, 50, 80)
#
# pot = Weapon('平底锅', 20)
# axe = Weapon('斧子', 50)
# stick = Weapon('双节棍', 65)
#
# pedal = Moto('小踏板', 60)
# yamaha = Moto('雅马哈', 80)
# bmw = Moto('宝马', 120)

# cjk.drive(pedal)
# dsn.drive(bmw)
# bod.drive(yamaha)
# cjk.ko1(bod)
# dsn.ko1(bod)
# bod.ko2(cjk, pot)
# bod.ko2(dsn, axe)
# cjk.ko3(dsn, bmw, pedal, stick)
# bod.ko3(dsn, pedal, yamaha, axe)


# sys.argv练习
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23


# 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
# 完成方法
# 计算圆形面积
# 计算圆形周长
import math


# class Circle(object):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         a = math.pi * pow(self.radius, 2)
#         log(f'圆形面积: {a}')
#
#     def circum(self):
#         c = 2 * math.pi * self.radius
#         log(f'圆形周长: {c}')
#
#
# c1 = Circle(5)
# c2 = Circle(10)
# c1.area()
# c1.circum()
# c2.area()
# c2.circum()


# 定义一个圆环类，计算圆环的周长和面积（升级题）。
# class Ring(object):
#     def __init__(self, short, long):
#         self.short = short
#         self.long = long
#
#     def circum(self):
#         c1 = 2 * math.pi * self.short
#         c2 = 2 * math.pi * self.long
#         log(f'周长: {c1 + c2}')
#
#     def area(self):
#         a1 = math.pi * pow(self.long, 2)
#         a2 = math.pi * pow(self.short, 2)
#         log(f'面积: {a1 - a2}')
#
#
# r = Ring(5, 9)
# r.circum()
# r.area()


# 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 登陆成功之后才创建用户对象
# 设计一个方法 修改密码
# class User(object):
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     def alter(self, password):
#         self.password = password
