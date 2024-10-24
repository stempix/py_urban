from private.test_runner import test_runner

def calculate_code(num):# Main calculation func
    pairs_list = []

    for head_pair_num in range(1, num):
        tail_pair_num = head_pair_num + 1
        while tail_pair_num < num:
            if head_pair_num + tail_pair_num > num:
                break
            if num % (head_pair_num + tail_pair_num) == 0:
                pairs_list.extend([head_pair_num, tail_pair_num])
            tail_pair_num += 1
    # Convert to string code format
    return "".join(str(number) for number in pairs_list)

test_data = tuple([num] for num in range(1, 21))

# Expected results
test_expect = (
    "",                                         # Test 1
    "",                                         # Test 2
    "12",                                       # Test 3
    "13",                                       # Test 4
    "1423",                                     # Test 5
    "121524",                                   # Test 6
    "162534",                                   # Test 7
    "13172635",                                 # Test 8
    "1218273645",                               # Test 9
    "141923283746",                             # Test 10
    "11029384756",                              # Test 11
    "12131511124210394857",                     # Test 12
    "112211310495867",                          # Test 13
    "1611325212343114105968",                   # Test 14
    "1214114232133124115106978",                # Test 15
    "1317115262143531341251161079",             # Test 16
    "11621531441351261171089",                  # Test 17
    "12151811724272163631545414513612711810",   # Test 18
    "118217316415514613712811910",              # Test 19
    "13141911923282183731746416515614713812911" # Test 20
)

test_runner(test_data, test_expect, calculate_code)

input_num = int(input("Enter first plate number: "))

if input_num not in range(3, 21):
    # Exclude wrong number
    print("Number is out of range!")
else:
    print("Your code:", calculate_code(input_num))