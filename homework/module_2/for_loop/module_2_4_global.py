numbers = [31, 38, 85, 52, 64, 10, 60, 69, 83, 67, 74, 50, 9, 84, 22]

primes = []
not_primes = []

for i in range(len(numbers)):
    # Откидываем 0, 1 (учитывая, что не будем работать с отрицательными числами
    # в рамках данной задачи)
    if numbers[i] < 2:
        continue
    is_prime = True
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Primes: ", primes)
print("Not primes: ", not_primes)