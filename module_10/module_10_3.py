import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _i in range(100):
            amount = random.randint(50, 500)
            try:
                with self.lock:  # Блокируем доступ к балансу при пополнении
                    self.balance += amount
                    time.sleep(0.001)  # Имитация задержки
                    print(f"Пополнение: {amount}. Баланс: {self.balance}")
                    # Если баланс 500 или больше, разблокируем
                    if self.balance >= 500 and self.lock.locked():
                        self.lock.release()
            except:
                pass

    def take(self):
        for _i in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                with self.lock:  # Блокируем при снятии
                    self.balance -= amount
                    time.sleep(0.001)  # Имитация задержки
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()  # Блокируем поток
                # self.deposit()
                self.lock.release()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')