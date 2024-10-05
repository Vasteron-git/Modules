
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(f"Этаж: { i } {self.name}")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __lt__(self, other):   #( <)
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
    def __le__(self, other):    #( <=):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
    def __gt__(self, other): #( >)
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
    def __ge__(self, other):  #( >=)
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
    def __ne__(self, other):  #( !=)
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        return self
    def __radd__(self, value):
         return House.__add__(self, value)
    def __iadd__(self, value):
        return House.__add__(self, value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}')
print(f'Название: {h2.name}, кол-во этажей: {h2.number_of_floors}')

print(House.__eq__(h1, h2)) # __eq__

House.__add__(h1, 10) # __add__
print(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}')
print(House.__eq__(h1, h2))

House.__iadd__(h1, 10) # __iadd__
print(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}')

House.__radd__(h2, 10) # __radd__
print(f'Название: {h2.name}, кол-во этажей: {h2.number_of_floors}')

print(House.__gt__(h1, h2)) # __gt__
print(House.__ge__(h1, h2)) # __ge__
print(House.__lt__(h1, h2)) # __lt__
print(House.__le__(h1, h2)) # __le__
print(House.__ne__(h1, h2)) # __ne__
