# 1. Write a decorator that ensures a function is only called by users with a specific role. 
# Each function should have an user_type with a string type in kwargs. Example:
# @is_admin
# def show_customer_receipt(user_type: str):
#     # Some very dangerous operation

# show_customer_receipt(user_type='user')
# > ValueError: Permission denied

# show_customer_receipt(user_type='admin')
# > function pass as it should be

def is_admin(func):
    def decorator(**kwargs):  
        if  kwargs["user_type"] != "admin":
            raise ValueError("Permission denied")
        else:
            return func(**kwargs)
    return decorator  
    

@is_admin
def show_customer_receipt(user_type: str):
    print("Access permitted")

# show_customer_receipt(user_type='user')
# show_customer_receipt(user_type='admin')


# 2. Write a decorator that wraps a function in a try-except block and prints an error if an error has happened. 
# Example:
# @catch_errors
# def some_function_with_risky_operation(data):
#     print(data['key'])


# some_function_with_risky_operation({'foo': 'bar'})
# > Found 1 error during execution of your function: KeyError no such key as foo

# some_function_with_risky_operation({'key': 'bar'})
# > bar

def catch_errors(func):
    def decorator(*args,**kwargs):     
        try: 
            func(*args,**kwargs)    
        except Exception as key:
            print(f"Found 1 error during execution of your function: KeyError no such key as {key}") 
    return decorator 

@catch_errors
def some_function_with_risky_operation(data):
    print(data["key"])

some_function_with_risky_operation({'foo': 'bar'})


# 3. Optional: Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.
#  It should work for all possible functions. Don`t forget to check the return type as well

# Example:
# @check_types
# def add(a: int, b: int) -> int:
#     return a + b

# add(1, 2)
# > 3

# add("1", "2")
# > TypeError: Argument a must be int, not str
from __future__ import annotations

def check_types(func):
    def decorator(*args):     
        type_dict = func.__annotations__
        for expected_type in type_dict:
            for real_type in args:
                if type_dict[expected_type] !=  type(real_type).__name__:
                    raise TypeError(f"Argument a must be int, not {type(real_type).__name__}") 
        
        func(*args)
    return decorator 

@check_types
def add(a: int, b: int) -> int:
    return a + b

add(1, (2,))


# 4. Optional: Create a function that caches the result of a function, 
# so that if it is called with the same argument multiple times, 
# it returns the cached result first instead of re-executing the function.

cache = [{"3+7":10},
         {"7+10":17},
         {"3+10":13},
         {"10+17":27}
    ]


def checking_cache(func):
    def decorator(*args):     
        if {f"{args[0]}+{args[1]}":sum(args)} in cache:
            _index = cache.index({f"{args[0]}+{args[1]}":sum(args)})
            return (cache[_index])[f"{args[0]}+{args[1]}"]
        else:
            cache.append({f"{args[0]}+{args[1]}":sum(args)})
            func(*args)   
    return decorator 

@checking_cache
def adding_res(x:int, y:int ) -> int:
    return x + y

adding_res(7,10)


from datetime import datetime as dt
import csv







def time_limit(func):

    def decorator():        
        time = dt.now()
        current_time = time.strftime("%a %b %d %H:%M")
        fieldnames = [f"{current_time}"]
        
        with open("limit.csv", "r") as file:
            reader = csv.DictReader(file)
            x = [row for row in reader]
            if len(x) == 0:
                count = 1
            for line in x:    
                if current_time in line:
                    count = int(line[current_time]) + 1
                else:
                    count = 1

        clean = open("limit.csv","w")
        clean.close()
        
        with open("limit.csv", "w") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({current_time:count})

        if count <= 3:
            count += 1 
            func()

    return decorator 

@time_limit
def some_function():
    print(111)

some_function()