import random

def code_gen(lenght:int) -> str:
    code = ''
    if type(lenght) == int:
        for i in range(lenght):
            sumb = chr(random.randint(48,123))
            code += sumb
        print(f'Your code: {code}')

code_gen(7)