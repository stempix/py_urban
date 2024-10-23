calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return tuple([len(string), string.upper(), string.lower()])

def is_contains(string, list_to_search):
    count_calls()
    return string.casefold() in [s.casefold() for s in list_to_search]

string_1 = "I am student of Urban Academy"
string_2 = "My name is Emil"
string_3 = "I study Python development"
string_4 = "My progress is great"
string_5 = "Python is simple"

print(string_info(string_1))
print(string_info(string_2))
print(string_info(string_3))
print(string_info(string_4))
print(string_info(string_5))

print(is_contains("Python", string_1.split()))
print(is_contains("Python", string_2.split()))
print(is_contains("Python", string_3.split()))
print(is_contains("Python", string_4.split()))
print(is_contains("Python", string_5.split()))

print(is_contains("is", string_1.split()))
print(is_contains("is", string_2.split()))
print(is_contains("is", string_3.split()))
print(is_contains("is", string_4.split()))
print(is_contains("is", string_5.split()))

print(calls)