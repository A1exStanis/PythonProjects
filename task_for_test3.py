def is_balanced(string):
    matching_brackets = {
        ']': '[',
        '}': '{',
        ')': '(',
    }

    stack = []

    for char in string:
        if char in '{([':
            stack.append(char)
        elif char in '})]':
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
    return len(stack) == 0


string1 = "{[()()]}"
string2 = "{[(])}"

print(is_balanced(string1))  # Виведе: True
print(is_balanced(string2))  # Виведе: False
