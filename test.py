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

def out_func():
    number = input("Type an integer number:")
    print(f"You typed:{number}.")
    return in_func(number)
def in_func(number):
    while type(number) != int:
        try:
            int_number = int(number)
            print(int_number)
            break
        except Exception:
            print("Something goes wrong, try to type an integer")
            number = input("Type an integer number:")
    
out_func()