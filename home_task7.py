# Create a class Product with properties name, price, and quantity.
# Create a child class Book that inherits from Product and adds a property author and a method called read.

class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name,price,quantity,author) -> None:
        super().__init__(name,price,quantity)
        self.author = author
    def read(self):
        print(f"If you want to read {self.name} author {self.author}, you need to pay {self.price}")


auth = Book("The Outsider", 355, 1,"Stephen King")

auth.read()


# Create a class Restaurant with properties name, cuisine, and menu. The menu property should be a dictionary 
# with keys being the dish name and values being the price. Create a child class FastFood that inherits from 
# Restaurant and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not) 
# and a method called order which takes in the dish name and quantity and returns the total cost of the order. 
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. 
# If the dish is not available or if the requested quantity is greater than the available quantity, 
# the method should return a message indicating that the order cannot be fulfilled.


class Restaurant:
    def __init__(self,name, cuisine, menu) -> None:
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru) -> None:
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru in menu
    
    def order(self, dish_name, dish_quantity):
        self.dish_name = dish_name
        self.dish_quantity = dish_quantity
        if self.dish_name in menu:
            numbers = menu[self.dish_name]
            if numbers["quantity"] >= self.dish_quantity:
                menu[self.dish_name]["quantity"] = numbers["quantity"] - self.dish_quantity
                return self.dish_quantity * numbers["price"]
            else:
                return "Requested quantity not available"
        else:
            return "Dish not available"
menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available
print(menu)


# (Optional) A Bank
# 1.    Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount.
#       A SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute and a method which adds interest to the account.
#       A CurrentAccount object, in addition to the attributes of an Account object, should have an overdraft limit attribute.
# 2.    Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be instances of the Account class,
#       the SavingsAccount class, or the CurrentAccount class. Create some test accounts (some of each type).
# 3.    Write an update method in the Bank class. It iterates through each account, updating it in the following ways:
#       Savings accounts get interest added (via the method you already wrote);
#       CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).
# 4.    The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.

class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

class SavingAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest
    def add(self):
        self.balance = self.balance + self.balance / 100 * self.interest
        
class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

class Bank:
    def __init__(self, accounts:list[Account]):
        self.accounts = accounts
    def uppdate(self,accounts):
        for account in accounts:
            if isinstance(account,SavingAccount):
                account.add()
                print(f"On your account {account.account_number}.You have {account.balance}")
            elif isinstance(account,CurrentAccount):
                print(f"On your account {account.account_number}.You have overdraft limit {account.overdraft_limit}")
            else:
                print(f"On your account {account.account_number}.You have {account.balance}")
        

a = SavingAccount(1000,101,25)
b = CurrentAccount(1000,102,300)
c = Account(1000,103)
banks = Bank([a,b,c])
banks.uppdate([a,b,c])