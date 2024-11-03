from fake_math import divide as fake_div
from math import inf
from private.test_runner import test_runner
from true_math import divide as true_div

error_word = "Ошибка!"

test_data = [
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [2, 1]
]

fake_test_expect = [
    error_word,
    0.0,
    error_word,
    1.0,
    2.0
]

true_test_expect = [
    inf,
    0.0,
    inf,
    1.0,
    2.0
]

print(f"Function {fake_div.__name__} from module {fake_div.__module__} testing:\n")
test_runner(test_data, fake_test_expect, fake_div)
print(f"Function {true_div.__name__} from module {true_div.__module__} testing:\n")
test_runner(test_data, true_test_expect, true_div)