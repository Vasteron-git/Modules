
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
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print("Значения не принадлежат классу House")
    def __lt__(self, other):   #( <)
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):    #( <=):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other): #( >)
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):  #( >=)
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):  #( !=)
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = self.number_of_floors + value
    def __radd__(self, value):
         return House.__add__(self, value)
    def __iadd__(self, value):
        return House.__add__(self, value)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(House.__str__(h1))
print(House.__str__(h2))

# __len__
print(House.__len__(h1))
print(House.__len__(h2))
