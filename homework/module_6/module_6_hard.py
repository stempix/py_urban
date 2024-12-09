from math import pi, sqrt
from collections.abc import Collection

class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled = False):
        if not self.__is_valid_sides(*sides):
            sides = [1] * self.sides_count
        if not isinstance(color, Collection) or len(color) != 3 or not Figure.__is_valid_color(*color):
            color = [0, 0, 0]
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return r in range(256) and g in range(256) and b in range(256)

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled = False):
        super().__init__(color, *sides, filled = filled)
        self.__radius = self._Figure__sides[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled = False):
        super().__init__(color, *Triangle.__correct_sides(sides), filled = filled)

    def set_sides(self, *new_sides):
        super().set_sides(*Triangle.__correct_sides(new_sides))

    def get_square(self):
        sides = self._Figure__sides
        p = len(self) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

    @staticmethod
    def __correct_sides(sides):
        if (len(sides) == 3 and
                not (sides[0] > sum(sides[1:]) or sides[1] > sides[0] + sides[2] or sides[2] > sum(sides[:2]))):
            return sides
        return []

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled = False):
        if len(sides) > 1:
            sides = [1]
        super().__init__(color, *([sides[0]] * self.sides_count), filled = filled)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(*(new_sides * self.sides_count))

    def get_volume(self):
        return self._Figure__sides[0] ** 3

# Символы для текста
bold_start = "\033[1m"
green_text = "\033[32m"
blue_text = "\033[34m"
res_set = "\033[0m"

# Проверки создания фигур
right_circle = Circle((100, 150, 200), 10)
print(
    f"{bold_start}{green_text}Параметры правильно заданного круга:{res_set}\n",
    f"\t{blue_text}Стороны: {right_circle.get_sides()}\n",
    f"\tЦвет: {right_circle.get_color()}\n",
    f"\tПлощадь: {right_circle.get_square()}{res_set}"
)
wrong_circle = Circle((150, 250, 350), 25, 10, 15)
print(
    f"{bold_start}{green_text}Параметры неправильно заданного круга:{res_set}\n",
    f"\t{blue_text}Стороны: {wrong_circle.get_sides()}\n",
    f"\tЦвет: {wrong_circle.get_color()}\n",
    f"\tПлощадь: {wrong_circle.get_square()}{res_set}"
)

right_triangle = Triangle((10, 20, 30), 10, 20, 30)
print(
    f"{bold_start}{green_text}Параметры правильно заданного треугольника:{res_set}\n",
    f"\t{blue_text}Стороны: {right_triangle.get_sides()}\n",
    f"\tЦвет: {right_triangle.get_color()}\n",
    f"\tПлощадь: {right_triangle.get_square()}{res_set}"
)
wrong_triangle_1 = Triangle((1, 2, 3), 10, 20, 40)
print(
    f"{bold_start}{green_text}Параметры первого неправильно заданного треугольника:{res_set}\n",
    f"\t{blue_text}Стороны: {wrong_triangle_1.get_sides()}\n",
    f"\tЦвет: {wrong_triangle_1.get_color()}\n",
    f"\tПлощадь: {wrong_triangle_1.get_square()}{res_set}"
)
wrong_triangle_2 = Triangle((256, -1, 0), 1, 2, 3, 4)
print(
    f"{bold_start}{green_text}Параметры второго неправильно заданного треугольника:{res_set}\n",
    f"\t{blue_text}Стороны: {wrong_triangle_2.get_sides()}\n",
    f"\tЦвет: {wrong_triangle_2.get_color()}\n",
    f"\tПлощадь: {wrong_triangle_2.get_square()}{res_set}"
)

right_cube = Cube((100, 100, 100), 5)
print(
    f"{bold_start}{green_text}Параметры правильно заданного куба:{res_set}\n",
    f"\t{blue_text}Стороны: {right_cube.get_sides()}\n",
    f"\tЦвет: {right_cube.get_color()}\n",
    f"\tОбъем: {right_cube.get_volume()}{res_set}"
)
wrong_cube = Cube((1, 2), 10, 20)
print(
    f"{bold_start}{green_text}Параметры неправильно заданного куба:{res_set}\n",
    f"\t{blue_text}Стороны: {wrong_cube.get_sides()}\n",
    f"\tЦвет: {wrong_cube.get_color()}\n",
    f"\tОбъем: {wrong_cube.get_volume()}{res_set}"
)

# Проверки установки цвета
right_color = (77, 88, 99)
wrong_color_1 = (0, 150, 300)
wrong_color_2 = (-1, -2, -3)
print(f"{bold_start}{green_text}Проверка установки цвета (изначальный цвет: {right_circle.get_color()}):{res_set}")
right_circle.set_color(*wrong_color_1)
print(f"\t{blue_text}Меняем на {wrong_color_1}: цвет не поменялся: {right_circle.get_color()}")
right_circle.set_color(*wrong_color_2)
print(f"\tМеняем на {wrong_color_2}: цвет не поменялся: {right_circle.get_color()}")
right_circle.set_color(*right_color)
print(f"\tМеняем на {right_color}: цвет поменялся: {right_circle.get_color()}{res_set}")

# Проверки установки сторон
print(f"{bold_start}{green_text}Проверка установки cторон круга "
      f"(изначальные стороны: {right_circle.get_sides()}):{res_set}")
right_circle.set_sides(10, 20 ,30)
print(f"\t{blue_text}Меняем на (10, 20, 30): стороны не поменялись: {right_circle.get_sides()}")
right_circle.set_sides(-5)
print(f"\tМеняем на (-5): стороны не поменялись: {right_circle.get_sides()}")
right_circle.set_sides(5)
print(f"\tМеняем на (5): стороны поменялись: {right_circle.get_sides()}{res_set}")

print(f"{bold_start}{green_text}Проверка установки cторон треугольника "
      f"(изначальные стороны: {right_triangle.get_sides()}):{res_set}")
right_triangle.set_sides(1)
print(f"\t{blue_text}Меняем на (1): стороны не поменялись: {right_triangle.get_sides()}")
right_triangle.set_sides(1, 2, -3)
print(f"\tМеняем на (1, 2, -3): стороны не поменялись: {right_triangle.get_sides()}")
right_triangle.set_sides(1, 2, 4)
print(f"\tМеняем на (1, 2, 4): стороны не поменялись: {right_triangle.get_sides()}")
right_triangle.set_sides(2, 3, 5)
print(f"\tМеняем на (2, 3, 5): стороны поменялись: {right_triangle.get_sides()}{res_set}")

print(f"{bold_start}{green_text}Проверка установки cторон куба "
      f"(изначальные стороны: {right_cube.get_sides()}):{res_set}")
right_cube.set_sides(-1)
print(f"\t{blue_text}Меняем на (-1): стороны не поменялись: {right_cube.get_sides()}")
right_cube.set_sides(1, 2)
print(f"\tМеняем на (1, 2: стороны не поменялись: {right_cube.get_sides()}")
right_cube.set_sides(15)
print(f"\tМеняем на (15): стороны поменялись: {right_cube.get_sides()}{res_set}")