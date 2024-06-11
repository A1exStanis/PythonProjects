def fibonacci(n):
    sum = 0
    digit_1 = 1
    digit_2 = 0
    for i in range(n):
        sum = digit_2 + digit_1
        digit_2 = digit_1 + digit_2
        digit_1 = sum - digit_1

    print(sum)


fibonacci(11)
