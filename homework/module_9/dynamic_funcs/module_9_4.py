from random import choice


# 1. Lambda function
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda l1, l2: l1 == l2, first, second)))

# 2. Closure
def get_advances_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything

writer = get_advances_writer('example.txt')
writer('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3. Callable class
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())