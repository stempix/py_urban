from collections.abc import Collection
from numbers import Number

def __is_list_numeric(int_list):
    for num in int_list:
        if not isinstance(num, Number):
            return False
    return True

def apply_all_func(int_list, *functions):
    if not isinstance(int_list, Collection):
        print(f"{type(int_list)} is not collection!")
        return
    if not __is_list_numeric(int_list):
        print("List must include only numeric values!")
        return
    result = dict()
    for func in functions:
        if not callable(func):
            print(f"{type(func)} is not callable!")
            continue
        result[func.__name__] = func(int_list)
    return result

print(apply_all_func(0, max, min))                      # int_list is not collection
print(apply_all_func([6, 20, 15, 9], max, min))         # all good
print(apply_all_func(['str', 20, 15, 9], max, min))     # int_list have not-numeric value
print(apply_all_func([6, 20, 15, 9], 1, sum, sorted))   # *functions have not-callable argument
print(apply_all_func([6, 20, 15, 9], len, sum, sorted)) # all good