def factorial(x):
    result = 1
    for i in range(2,x+1):
        result *= i
    return result

def comb(n,k):
    result = factorial(n)/(factorial(k)*factorial(n-k))
    return result

print(comb(5, 3))