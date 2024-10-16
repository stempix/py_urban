numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for j in range(len(primes)):
        if numbers[i] % primes[j] == 0:
            is_prime = False

    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Prime numbers: ", primes)
print("Not prime numbers: ", not_primes)