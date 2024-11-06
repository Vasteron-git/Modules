
from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)
# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'a', encoding='utf-8') as file:
            for str in data_set:
                file.write(f"{str}\n")
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = []
        self.set_words(words)
    def set_words(self, new_list):
        self.words = list(new_list)
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

