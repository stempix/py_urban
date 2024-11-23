import io
from inspect import isfunction, ismethod
from io import StringIO
import sys

# Первоначальная реализация для личного пользования.
# Будет дополняться по мере необходимости.
# Пока используются следующие допущения:
#   1. Тестируются только функции с аргументами;
#   2. Элементы test_data - списки или кортежи с аргументами функции.

def test_runner(
        test_data = None,
        test_return_expect = None,
        func = None,
        enable_output = False,
        test_output_expect = None):
    if not isfunction(func) and not ismethod(func):
        print("Bad 'func' argument!")
        exit()
    passed_cnt, failed_cnt, total_cnt = 0, 0, len(test_data)
    for test_idx in range(total_cnt):
        print(f"Test {test_idx + 1}:")
        print(f"\tData: {test_data[test_idx]}")
        # Suppressing the output
        suppressed_output = StringIO()
        sys.stdout = suppressed_output
        # Testing func run
        test_result = func(*test_data[test_idx])
        # Returning default output
        sys.stdout = sys.__stdout__
        test_passed = True
        if enable_output:
            suppressed_output.seek(0)
            print(f"\tOutput: {suppressed_output.read().replace('\n', '\t').strip()}")
        if test_output_expect:
            if len(test_data) != len(test_output_expect):
                print("Bad test output expect data!")
                exit()
            suppressed_output.seek(0)
            test_passed = suppressed_output.read().replace('\n', '\t').strip() == test_output_expect[test_idx].strip()
        if not test_result is None:
            print(f"\tReturned value: {test_result}")
        if test_return_expect:
            if len(test_data) != len(test_return_expect):
                print("Bad test return expect data!")
                exit()
            test_passed = test_passed and test_result == test_return_expect[test_idx]
        if test_passed:
            print(f"TEST {test_idx + 1} PASSED!")
            passed_cnt += 1
        else:
            print(f"TEST {test_idx + 1} FAILED!")
            failed_cnt += 1

    print(f"\nTEST STATISTICS:\n\tTotal:\t{total_cnt}\n\tPassed:\t{passed_cnt}\n\tFailed:\t{failed_cnt}\n")

    if total_cnt == passed_cnt:
        return True
    else:
        return False