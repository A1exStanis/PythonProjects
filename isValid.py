# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    opcl = dict(('()', '[]', '{}'))
    stack = []
    for idx in s:
        if idx in '([{':
            stack.append(idx)
        elif len(stack) == 0 or idx != opcl[stack.pop()]:
            return False
    return len(stack) == 0