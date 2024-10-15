my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

iter_num = 0
while iter_num != len(my_list):
    current_num = my_list[iter_num]
    iter_num += 1
    if current_num >= 0:
        if current_num == 0:
            continue
        print(current_num)
    else:
        break