
# Given two integer numbers, return their product only
# if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

# one = int(input())
# two = int(input())
# if one * two <= 1000:
#     print(one * two)
# else:
#     print(one+two)


# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

# number = int(input("Type the number: "))
# for i in range(number):
#    if i == 0:
#         print("Current number:",i, "Previous number:", i, 'Sum:', i)
#    print("Current number:",i, "Previous number:", i-1, 'Sum:', i*2-1)


# num = 123
# print(num%10*100+num%100//10*10+num//100)

# 3 < 4

# 10 > 5

# 42 == int("42")


# print('He said \'Bla bla bla \'')



# The program receives the user's name and age from the input. 
# Then you need to display the name and age in one line in several ways: 

# - by listing all the parameters in the print function
# - by formatting a string using the format function
# - by formatting a string with f-string

# The string should look like this: 
# `"Your name is {name} and your {age} years old"`

# name = input()
# age = input()

# print("Your name is", name, "and your", age, "years old")
# print("Your name is {name} and your {age} years old".format(name = name, age = age))
# print(f"Your name is {name} and your {age} years old")


# string_1 = "Animals  "
# print(string_1.lower())
# string_2 = "  Badger"
# print(string_2.upper())
# string_3 = "   HoneyPot   "
# print(string_3.rstrip())
# print(string_3.lstrip())
# print(string_3.strip())



# string_1 = "Bear"
# string_2 = "bear"
# string_3 = "BEAR"
# string_4 = "bEar"
# print(string_1.startswith("Be"))
# print(string_2.startswith("Be"))
# print(string_3.startswith("Be"))

# #Convert these bear-like rows with methods from the previous exercise to have a positive result for each row.
# formatted_string2 = string_2.replace("b","B")
# print(formatted_string2)
# formatted_string3 = "Be"+string_3[2:]
# print(formatted_string3)


# line = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
# line = line.replace('X','').replace('x', "")


# print(line[::-1])

# print(False == (not True))     
# print((True and False) == (True and False))     
# print(not (True and "A" == "B"))

# 2. Make a solution for Wheat and chessboard
#  problem. Represent a solution in tons.
#  Assume that one grain of wheat weights 0.065 gram

# 5. (Optional): Write a Python program to get the next day of a given date.
# Get the day, month and year from the user input.
# Don`t use datetime module for that

# Expected Output:

#     **Input a year:** 2022                                                     

#     **Input a month [1-12]:** 8                                               

#     **Input a day [1-31]:** 23                                           

#     The next date is [yyyy-mm-dd] 2022-8-24

# 

# Write a function called `find_primes` that takes in two integers a and b 
# and returns a list of all the prime numbers between a and b (inclusive).

# def find_primes(a:int,b:int):
#     for i in range(a,b+1):
#         for q in range (2,i):
#             if i%q == 0:
#                 continue
#             print(i)



# find_primes(1,10)


# Write a program that asks the user to enter an integer and convert it to an int. The program should have 2 functions.
# The first function should ask the user to input information and return inputted value. The second function receives the inputted value and converts it to int. 
# If the user enters something that is not an integer, this function should catch an error and ask the user to enter an integer again. 
# if the user inputs an integer, the program should print this number and quit w/o any error.

# def out_func():
#     number = input("Type an integer number:")
#     print(f"You typed:{number}.")
#     return in_func(number)
# def in_func(number):
#     while type(number) != int:
#         try:
#             int_number = int(number)
#             print(int_number)
#             break
#         except Exception:
#             print("Something goes wrong, try to type an integer")
#             number = input("Type an integer number:")
#
# out_func()

# x = 121
# x = list(str(x))
# for i, il in enumerate(x):
#     if il != x[-i]:
#         print(False)
#     print(True)

# l1 = [2,4,3]
# l2 = [5,6,4]
# l3 = []
# sum = 0
# for i, il in enumerate(l1):
#     if il+l2[i]>=10:
#         l3.append((il+l2[i])%10+sum)
#         sum = 1
#     else:
#         l3.append(il+l2[i]+sum)
#         sum = 0
# print(l3)

# count_list = []
# for i, il in enumerate(s):
#     l = 0
#     for q, ql in enumerate(s[i:]):
#         if il != ql or i == q:
#             l += 1
#         else:
#             count_list.append(l)
#     print (count_list)
#         while q>=i and il!=ql
# s = 'abcb'
# count_list = []
# if len(s) != 0:
#     l = 0
#     for i, il in enumerate(s):
#         l = 0
#         count = 1
#         if count == len(s):
#             l += 1
#             count_list.append(l)
#             break
#         for q, ql in enumerate(s[i:]):
#             if il != ql or q == 0:
#                 l += 1
#                 count += 1
#             if q==s[-1]:
#                 count_list.append(l)
#                 l = 0
#                 break
#     print(count_list)
# else:
#     print(0)

# def findMedianSortedArrays( nums1: list, nums2: list) -> float:
#     compl_nums = nums1 + nums2
#     compl_nums.sort()
#     long = len(compl_nums)
#     if long % 2 == 0:
#         median = int(long / 2)
#         new_list = compl_nums[(median - 1):(median + 1)]
#         result = sum(new_list) / 2
#     else:
#         q = long/2
#         x = round(long/2)
#         median = int(x)
#         result = compl_nums[(median)]
#     print(result)
#
#
# findMedianSortedArrays(nums1=nums1,nums2=nums2)

# def longestPalindrome(s: str) -> str:
#     result = ''
#     resLen = 0
#     long = len(s)
#     for i in range(long):
#         l, r = i, i + 1
#         while l >= 0 and r < long and s[l] == s[r]:
#             if r - l + 1 > resLen:
#                 result = s[l:r + 1]
#                 resLen = r - l + 1
#             l -= 1
#             r += 1
#         l, r = i, i
#         while l >= 0 and r < long and s[l] == s[r]:
#             if r - l + 1 > resLen:
#                 result = s[l:r + 1]
#                 resLen = r - l + 1
#             l -= 1
#             r += 1
# #     return result
# longestPalindrome(s='ac')

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
#         print (result)
#     else:
#         while x > 0:
#             y = x % 10
#             new_list.append(y)
#             x = x // 10
#             long = len(new_list)
#             for i in range(long, 0, -1):
#                 result += i * 10 ** (long - 1)
#                 long -= 1
#             print(-(result))
#
# # reverse(120)
#
#
# def reverse_(x:int) -> int:
#     minus = '-'
#     if abs(x) == x:
#         minus = ''
#     result = ''
#     x = str(abs(x))
#     for i in x[::-1]:
#         result += i
#     print(int(minus + result))
#
# # reverse_(-120)
# q = -2147483412
# print(q.bit_length())
#
# print(2**31)


# def longestCommonPrefix(strs: list) -> str:
#     i = 0
#     result = ''
#     while strs[0][i] == strs[1][i] == strs[2][i]:
#         i += 1
#         result = result + strs[0][i]
#     return result
#
#
#
# strs = ["flower","flow","flight"]
# longestCommonPrefix(strs=strs)


# def isMatch(s: str,p: str) ->bool:
#     def dfs(i, j):
#         if i >= len(s) and j >= len(p):
#             return True
#         if j >= len(p):
#             return False
#
#         match = i < len(s) and (s[i] == p[j] or p[j] == '.')
#         if j+1 < len(p) and p[j+1] == '*':
#             return (dfs(i, j+2) or (match and dfs(i+1,j)))
#         if match:
#             return dfs(i+1, j+1)
#         return False
#     return dfs(0,0)


# print(isMatch('aab','c*a*b'))

# list_ = [1, 8, 6, 2, 5, 4, 8, 3, 7]
list_ = [1,1]


# def maxArea(height: list) -> int:
#     # left = len(height) - 1
#     contain_list = []
#     # long = len(height) - 1
#     # for i in height:
#     #     max_height = min(i, height[-1])
#     #     area = max_height * long
#     #     contain_list.append(area)
#     #     long -= 1
#     # print(contain_list)
#     for i in height:
#         for q in height:
#             index_i = height.index(i)
#             index_q = height.index(q)
#             if index_i != index_q:
#                 contain_list.append(min(i, q)*abs(index_i-index_q))
#     print(max(contain_list))
#
#
# maxArea(list_)

#
# s='()'
# if len(s)%2 == 0:
#     for i in range(len(s)-1):
#         q = s[i:i+2]
#         print(q[::-1])
#         if q is q[::-1]:
#             s = s[i+2]
#             continue
#         if s == []:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(False)


# dict_ = {
#     'q':'q'
# }
# if 'q' in dict_.keys():
#     print(True)

s = '({][})'


# def isValid(self, s: str) -> bool:
#     opcl = dict(('()', '[]', '{}'))
#     stack = []
#     for idx in s:
#         if idx in '([{':
#             stack.append(idx)
#         elif len(stack) == 0 or idx != opcl[stack.pop()]:
#             return False
#     return len(stack) == 0
#
# isValid(s)


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Hello')
#         result = func(*args, **kwargs)
#         print('Bye')
#         return result
#     return wrapper
#
# @my_decorator
# def say_Q(name: str) -> None:
#     print(f'Q {name}')
#
# say_Q('Alex')


from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Генерація пари ключів
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

# Серіалізація ключів для збереження або передачі
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


# Шифрування повідомлення
# message = b"This is a secret message."
# encrypted_message = public_key.encrypt(
#     message,
#     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
# )
#
# print(encrypted_message)
#
#
# # Дешифрування повідомлення
# decrypted_message = private_key.decrypt(
#     encrypted_message,
#     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
# )
#
# print(decrypted_message)  # Виведе: b"This is a secret message."


from datetime import datetime as dt


def time_dec(func):
    def wrapper(*args, **kwargs):
        print(dt.time)
        func(*args, **kwargs)
        print(dt.time)
        return time_dec
    return wrapper



@time_dec
def use_null(n):
    for i in range(n):
        print(0)


# use_null(5)


q = [1,3,3,45,17,3,45]

print(set(q))
q = set(q)
q = list(q)
print(q)