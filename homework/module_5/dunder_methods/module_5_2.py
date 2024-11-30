from private.test_runner import test_runner

class House:
    def __init__(self, _name, _floors_num):
        self.name = _name
        self.number_of_floors = _floors_num

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Горский', 18)
h2 = House('Ботанический сад', 33)

test_return_expect = [
    18,
    33,
    "Название: ЖК Горский, кол-во этажей: 18",
    "Название: Ботанический сад, кол-во этажей: 33"
]

test_runner(func=h1.__len__, test_return_expect=test_return_expect[0])
test_runner(func=h2.__len__, test_return_expect=test_return_expect[1])
test_runner(func=h1.__str__, test_return_expect=test_return_expect[2])
test_runner(func=h2.__str__, test_return_expect=test_return_expect[3])
