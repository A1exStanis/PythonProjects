# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.

#
# def reverse(x: int) -> int:
#     result = 0
#     new_list = []
#     if abs(x) == x:
#         while x > 0:
#             y = x % 10
#             new_list.append(y)
#             x = x // 10
#         long = len(new_list)
#         for i in new_list:
#             result += i * 10**(long-1)
#             long -= 1
#         if result.bit_length()>=32:
#             return 0
#         return result
#     else:
#         while x > 0:
#             y = x % 10
#             new_list.append(y)
#             x = x // 10
#             long = len(new_list)
#             for i in range(long, 0, -1):
#                 result += i * 10 ** (long - 1)
#                 long -= 1
#             result = -result
#             if result.bit_length() >= 32:
#                 return 0
#             return result

# reverse(120)
#
#
# def reverse_(x: int) -> int:
#     minus = '-'
#     if abs(x) == x:
#         minus = ''
#     result = ''
#     x = str(abs(x))
#     for i in x[::-1]:
#         result += i
#     result = int(minus + result)
#     if result.bit_length() >= 32:
#         return 0
#     return result

# reverse_(-120)
# l = []
# s = '0-1'
# x = ''
# r = -1
# for i in range(1, len(s)+1):
#     try:
#         q = s[:len(s)-i+1]
#         x = int(q)
#         print(x)
#     except:
#         continue
s = '42'
s = s.lstrip()
if s:
    print (0)
i = 0
sign = 1
if s[i] == '+':
    i += 1
elif s[i] == '-':
    i += 1
    sign = -1
    pars = 0

while i < len(s):
    cur = s[i]
    if not cur.isdigit():
        break
    else:
        pars = pars * 10 + int(cur)
    i += 1

if pars > 2 ** 31 - 1:
     print(2 ** 31 - 1)
elif pars <= -2 ** 31:
    print(-2 ** 31)
else:
    print(pars)
