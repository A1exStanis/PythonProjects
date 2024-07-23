from string import digits
from time import perf_counter
from timeit import timeit
from abc import ABC, abstractmethod


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
        self.__area = self.__side ** 2

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side ** 2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.__side * 4
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
        return self.a * self.b

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

    def __len__(self):
        return abs(self.x - self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# p3 = Point(3, 5)
# print(p1 == p2)
# print(p2 == p3)
# print(hash(p1))
# print(hash(p2))
# print(hash(p3))
# print(bool(Point(1, 0)))
# print(bool(Point(0, 0)))


class Counter:
    def __init__(self):
        self.count = 0
        self.summa = 0
        self.length = 0
        print(f'Init object {self}')

    def __call__(self, *args, **kwargs):
        self.count += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Call used {self.count} times')

    def average(self):
        return self.summa / self.length


# a = Counter()
# a(12, 3, 5)
# a(1, 2, 3)
# print(a.average())


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Function worked {finish - start}')
        return result


@Timer
def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


# print(factorial(12))


class Vector:
    def __init__(self, **kwargs):
        self.values = dict(kwargs)
        print(self.values)

    def __getitem__(self, item):
        if item in self.values:
            return self.values[item]
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key in self.values:
            self.values[key] = value
        else:
            raise KeyError

    def __delitem__(self, key):
        if key in self.values:
            del self.values[key]
        else:
            raise KeyError


my_dict = {
    'q': 1,
    'w': 2,
    'e': 3
}
# p1 = Vector(**my_dict)
# print(p1["w"])
# p1["w"] = 10
# print(p1["w"])
# del p1['w']
# print(p1["w"])


class Marks:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        mark = self.value[self.index]
        self.index += 1
        return mark


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


# m = [3, 5, 4, 5]
# alex = Student('Alex', 'Stanis', m)
# for i in alex:
#     print(i)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = name

    def __str__(self):
        return f'Person - {self.name} {self.surname}'


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor - {self.name} {self.surname}'


# d = Doctor('Alex', 'Stanis', 22)
# print(d)
# print(d.age)


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


# p1 = PointSlots(3, 4)
# print(p1.__sizeof__())


def check_time_point():
    s = Points(3, 4)
    s.x = 100
    s.x
    del s.x


def check_time_pointslots():
    s = PointSlots(3, 4)
    s.x = 100
    s.x
    del s.x


# print(timeit(check_time_point))
# print(timeit(check_time_pointslots))


class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# counter = CountUp(5)
# for number in counter:
#     print(number)


# Визначаємо метаклас
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Створення класу {name} з метакласом {cls.__name__}")
        dct['greeting'] = 'Hello, World!'  # Додаємо новий атрибут до класу
        return super().__new__(cls, name, bases, dct)


# Створюємо клас з використанням метакласу
class MyClass(metaclass=MyMeta):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"{self.greeting}, {self.name}!"


# Створюємо екземпляр класу
obj = MyClass('Python')
#
# print(obj.greet())  # Виведе: Hello, World!, Python!

#
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance...")
        instance = super().__new__(cls)  # Allocate memory for the new instance
        return instance

    def __init__(self, value):
        print("Initializing instance...")
        self.value = value
#
#
# obj = MyClass(10)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2

    def perimetr(self):
        return 3.14 * self.r * 2


cir1 = Circle(6)
print(cir1.perimetr())
print(cir1.area())
