log = print


class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.blood = 100
        self.wise = 100

    def eat(self):
        log(f'{self.name} is eating {self.food}')

    def drink(self):
        log(f'{self.name} is drinking {self.food}')


class Cat(Animal):
    def eat(self):
        self.blood += 100
        Animal.eat(self)

    def climb(self):
        log(f'{self.name} is climbing')
        self.drink()


bai = Cat('xiaobai', 'catfood')
bai.eat()
bai.climb()
log(bai.__dict__)
