
class Animal:
    def __init__(self, name, alive = True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    def eat(self, food):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        Plant.__init__(self, name)

class Fruit(Plant):
    def __init__(self, name):
        Plant.__init__(self, name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

























