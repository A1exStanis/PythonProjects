from string import digits


class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be integer or float')
        self.__side = value
        self.__area = self.__side**2

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side**2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.__side*4
        return self.__perimeter


# a = Square(4)
# print(a.area)
#
# a.side = 12
# print(a.area)
# print(a.perimeter)


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.__secret_line = 'It`s a secret line!'

    @property
    def secret(self):
        s = input('Enter your password: ')
        if s == self.__password:
            return self.__secret_line
        else:
            raise ValueError('Access denied')

    @property
    def password(self):
        return self.password

    @staticmethod
    def include_number(password):
        for i in digits:
            if i in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print(len(value))
        if not isinstance(value, str):
            raise TypeError('Password must be string type')
        if len(value) > 20:
            raise ValueError('Password length must contain less then 20 symbols')
        if len(value) < 5:
            raise ValueError('Password length must contain more then 5 symbols')
        if not User.include_number(value):
            raise ValueError('Password mus include at least 1 digit')

        self.__password = value


# a1 = User('Alex', 'sem1q')
# print(a1.secret)


class Hi:
    def __init__(self, name):
        self.name = name

    @classmethod
    def class_hello(cls):
        print(f'Hello {cls}')


# q2 = Hi('Johnny')
# q2.class_hello()


class DepartmentIt:
    PYTHON_DEV = 3
    GO_DEV = 2

    @property
    def info_prop(self) -> None:
        print(self.PYTHON_DEV, self.GO_DEV)


# q = DepartmentIt()
# q.info_prop
# DepartmentIt().info_prop


class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Employee {self.name}'

    def __str__(self):
        return f'{self.name}'


# w = Employee('Jack')
# str(w)


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.balance - other
        if isinstance(other, BankAccount):
            return self.balance - other.balance
        raise NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.balance / other
        if isinstance(other, BankAccount):
            return self.balance / other.balance
        raise NotImplemented


# a = BankAccount('Alex', 700)
# b = BankAccount('Michel', 30)

# print(a+100)
# print(a+b)
# print(a-100)
# print(a-b)
# print(a*100)
# print(a*b)
# print(a/100)
# print(a/b)


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a*self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b
        if isinstance(other, (int, float)):
            return self.area == other
        raise NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other
        raise NotImplemented

    def __ge__(self, other):
        return self == other or self > other


# a = Rectangle(1, 2)
# b = Rectangle(3, 5)
# print(a > b)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (isinstance(other, Point) and
                self.x == other.x and self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# p3 = Point(3, 5)
# print(p1 == p2)
# print(p2 == p3)
# print(hash(p1))
# print(hash(p2))
# print(hash(p3))
