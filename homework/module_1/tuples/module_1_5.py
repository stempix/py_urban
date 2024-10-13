immutable_var = (1, 'two', True, [1, 'two', True])
print(immutable_var)

# immutable_var[1] = 'one'          # нельзя, т.к. кортеж неизменен
immutable_var[3][1] = 'index one'   # можно, т.к. элементы внутри кортежа могут изменяться (если эти элементы изменяемые)
# immutable_var[1][1] = '&'         # нельзя, т.к. строка - тоже неизменный тип данных

mutable_list = [1, 'two', True]
mutable_list[0] = 2
mutable_list[1] = 'three'
mutable_list[2] = False
print(mutable_list)