import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100  # Вражины
        self.days = 0
    def run(self):
        print(f"{self.name}, на нас напали!")
        time.sleep(0.1)
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончились!")
