def calculate_code(num):
    # Main calculation func
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

def test_module_2_hard():
    # Expected results
    expected_values = [
        "",
        "",
        "12",
        "13",
        "1423",
        "121524",
        "162534",
        "13172635",
        "1218273645",
        "141923283746",
        "11029384756",
        "12131511124210394857",
        "112211310495867",
        "1611325212343114105968",
        "1214114232133124115106978",
        "1317115262143531341251161079",
        "11621531441351261171089",
        "12151811724272163631545414513612711810",
        "118217316415514613712811910",
        "13141911923282183731746416515614713812911"
    ]
    # Test
    test_success_list = [False] * 20
    test_success_list[0] = calculate_code(0) == expected_values[0]
    test_success_list[1] = calculate_code(-1) == expected_values[1]
    for i in range(2, 20):
        test_success_list[i] = calculate_code(i + 1) == expected_values[i]

    return test_success_list

# Run tests
test_result = test_module_2_hard()
if all(test_result):
    print("All tests passed")
else:
    for iTest in range(len(test_result)):
        print("Test", iTest + 1, "failed!")
    exit()

input_num = int(input("Enter first plate number: "))

if input_num not in range(3, 21):
    # Exclude wrong number
    print("Wrong number")
else:
    print("Your code:", calculate_code(input_num))