from private.test_runner import test_runner

def get_multiple_digits(number):
    if number == 0:
        return 0
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    return first * get_multiple_digits(int(str_number[1:]))

test_data = (
    [0],        # Test 1
    [1],        # Test 2
    [11],       # Test 3
    [1234],     # Test 4
    [102],      # Test 5
    [40203],    # Test 6
    [000]       # Test 7
)

test_expect = (
    0,  # Test 1
    1,  # Test 2
    1,  # Test 3
    24, # Test 4
    2,  # Test 5
    24, # Test 6
    0   # Test 7
)

test_runner(test_data, test_expect, get_multiple_digits)