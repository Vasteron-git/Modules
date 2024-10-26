import math


class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = color
        self.filled = True
        self.set_sides(*sides)
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if isinstance(i, int) and 0 <= i <= 255:
                return True
            else:
                return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
    def __is_valid_sides(self, *new_sides):
        for side in new_sides:
            if isinstance(side, int) and len(new_sides) == self.sides_count and side > 0:
                return True
            else:
                return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 1
        if len(sides) == self.sides_count:
            self.__sides = [sides[0]]
        else:
            self.__sides = [1]
    def radius(self):
            return self.__sides[0] / (2 * math.pi)
    def get_square(self):
        return math.pi * (self.radius() ** 2)
class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 3
        if len(self.__sides) == self.sides_count:
            self.__sides = list(self.__sides)
        else:
            self.__sides = [1, 1, 1]
    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
class Cube(Figure):
    def __init__(self, color, side_length):
        self.sides_count = 12
        super().__init__(color, side_length)
        self.__sides =  [side_length] * self.sides_count
    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
