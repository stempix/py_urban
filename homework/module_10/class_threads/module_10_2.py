import threading
import time

class Knight(threading.Thread):
    __enemies_count = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        day_cnt = 0
        while self.__enemies_count:
            day_cnt += 1
            self.__enemies_count -= self.power
            print(f"{self.name} сражается {day_cnt}-й день, осталось {self.__enemies_count} войнов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {day_cnt} дней (дня)!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончены!")