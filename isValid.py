# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:

#


def isValid(s: str) -> bool:
    opcl = dict(('()', '[]', '{}'))
    stack = []
    for idx in s:
        if idx in '([{':
            stack.append(idx)
        elif len(stack) == 0 or idx != opcl[stack.pop()]:
            return False
    return len(stack) == 0