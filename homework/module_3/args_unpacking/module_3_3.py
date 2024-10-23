def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(3, 'Three')
print_params(4, 'Four', False)
print_params(a = 'Five', b = False, c = 5)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [6, 'Six', [True, False]]
values_dict = {
    'a': False,
    'b': 7,
    'c': 'Seven'
}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Eight', 8]
print_params(*values_list_2, 42)
print_params(42, *values_list_2)