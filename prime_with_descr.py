def prime_with_des(x):
    dividers = []
    primes = []
    is_prime = True
    numbers = range(1, x)
    for i in numbers:
        if x % i == 0:
            dividers.append(i)
            is_prime = False
    return f'Is prime:{is_prime}, got dividers {dividers}'


print(prime_with_des(30))