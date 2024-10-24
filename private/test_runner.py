from inspect import isfunction

# Первоначальная реализация для личного пользования.
# Будет дополняться по мере необходимости.
# Пока используются следующие допущения:
#   1. Тестируются только функции с аргументами;
#   2. Элементы test_data - списки или кортежи с аргументами функции.

def test_runner(test_data = None, test_expect = None, func = None):
    if not isfunction(func):
        print("Bad 'func' argument!")
        exit()
    if len(test_data) != len(test_expect):
        print("Bad test data!")
        exit()

    passed_cnt, failed_cnt, total_cnt = 0, 0, len(test_data)
    for test_idx in range(total_cnt):
        print(f"Test {test_idx + 1}:")
        print(f"\tData: {test_data[test_idx]}")
        test_result = func(*test_data[test_idx])
        print(f"\tOutput: {test_result}")
        if test_result == test_expect[test_idx]:
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