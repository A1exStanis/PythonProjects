import string
import random

def passcode(lenght = 8) -> None:
    code = ''
    for i in range(lenght):
        digit = random.randint(0,51)
        if code.count(string.ascii_letters[digit])== 0:
            code = code + string.ascii_letters[digit]
        else:
            while code.count(string.ascii_letters[digit]) != 0:
                if code.count(string.ascii_letters[digit+1]) == 0 and digit != 51:
                    code = code + string.ascii_letters[digit+1]
                    break
                elif digit == 51 and code.count(string.ascii_letters[digit-1]) == 0:
                    code = code + string.ascii_letters[digit-1]
                    break
    print(code)

# passcode()

def q():
    while True:
        print(1)

q()