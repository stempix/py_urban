from private.test_runner import test_runner
import collections.abc as cabc
import numbers

def calc_struct_sum(*args):
    result = 0

    for item in args:
        if isinstance(item, (numbers.Number, bool)):
            result += item
        elif isinstance(item, str):
            result += len(item)
        elif isinstance(item, cabc.Sequence):
            result += calc_struct_sum(*item)
        elif isinstance(item, set):
            result += calc_struct_sum(*tuple(item))
        elif isinstance(item, dict):
            result += calc_struct_sum(*item.keys(), *item.values())

    return result

test_data = [
    [
        [1, 2, {2.75, (True, False)}],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ],              # Test 1
    [[], {}, ()],   # Test 2
    [],             # Test 3
    ['']            # Test 4
]

test_expect = [
    99.75, # Test 1
    0,  # Test 2
    0,  # Test 3
    0   # Test 4
]

test_runner(test_data, test_expect, calc_struct_sum)