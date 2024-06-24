def simple_number(number: int) -> bool:
    long = [i for i in range(1, number//2+1)]
    if len(long) == 0:
        return True
    for q in long:
        if number % q == 0 and q != 1:
            return False
    return True


print(simple_number(4))
