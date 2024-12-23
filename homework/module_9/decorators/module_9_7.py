def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        d = 2
        while d ** 2 <= result and result % d != 0:
            d += 1
        print("Простое" if (d ** 2 > result) else "Составное")
        return result

    return wrapper

@is_prime
def sum_three(*numbers):
    return sum(numbers)

result = sum_three(2, 3, 6)
print(result)