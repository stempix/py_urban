import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            addition = random.randint(50, 500)
            self.balance += addition
            print(f"Пополнение: {addition}. Баланс: {self.balance}")
            time.sleep(0.001)
            if self.balance > 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for _ in range(100):
            withdrawal = random.randint(50, 500)
            print(f"Запрос на {withdrawal}")
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Снятие: {withdrawal}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')