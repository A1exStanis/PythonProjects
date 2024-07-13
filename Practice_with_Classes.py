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


a = Square(4)
print(a.area)

a.side = 12
print(a.area)
print(a.perimeter)


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


a1 = User('Alex', 'sem1q')
print(a1.secret)
