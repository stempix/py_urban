first = ['Strings', 'Student', 'Computers', 'Fourth element']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s1) - len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2))
second_result = (len(first[idx]) == len(second[idx])
                 # Добавлена проверка на длину, чтобы не словить обращение по несуществующему индексу
                 # в случае len(first) != len(second)
                 for idx in range(len(first) if len(first) <= len(second) else len(second)))

print(list(first_result))
print(list(second_result))