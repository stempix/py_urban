class Car:
    __NUMBERS_LENGTH = 6

    def __init__(self, model, vin, numbers):
        self.model = model
        if Car.__is_valid_vin(vin):
            self.__vin = vin
        if Car.__is_valid_numbers(numbers):
            self.__numbers = numbers

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип VIN-номера")
        if vin_number not in range(1_000_000, 10_000_000):
            raise IncorrectVinNumber("Неверный диапазон для VIN-номера")
        return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != Car.__NUMBERS_LENGTH:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, msg):
        self.message = msg

class IncorrectCarNumbers(Exception):
    def __init__(self, msg):
        self.message = msg

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')