# Задача 1.
# Створити клас Person, в метод ініціалізації передається name.
#  Створити:
#  метод activity, в якому викликати raise NotImplementedError,
#  метод activity_and_title, який виводить разом:
# name екземпляру,
# результат метод activity.
# Від нього наслідувати:
# клас BusinessAnalyst
# клас Programmer
# клас Tester
# В кожному з класів переозначити метод activity, повертати текст, відповідно:
# « : пише текст »
# « : пише код »
# « : ловить баги»
# Створити список екземплярів (від кожного класу - екземпляр).
# В циклі запусити виклик методу activity_and_title().


class Person:

    def __init__(self, name):
        self.name = name

    def activity(self):
        raise NotImplementedError('метод activity викликати raise NotImplementedError')

    def activity_and_title(self):
        print(f'{self.name} {self.activity()}')


class Business_Analyst(Person):

    def activity(self):
        return f' : пише текст '


class Programmer(Person):
    def activity(self):
        return f' : пише код '


class Tester(Person):
    def activity(self):
        return f' : ловить баги '


people = [
    Business_Analyst('Inna'),
    Programmer('Tetiana'),
    Tester('Andrii')
]

for person in people:
    person.activity_and_title()

# Як у відео, малювання, лише додати створення 6,8, та багатокутника (задається к-сть сторін).

import turtle as t


def draw(sides, side_lenght):
    angle = 360 / sides
    for i in range(sides):
        t.forward(side_lenght)
        t.left(angle)


# screen = t.Screen()
# draw(6, 50)
# t.penup()
#
# t.goto(100, 100)
# t.pendown()
# draw(8, 50)
# t.penup()
# t.goto(200, 200)
# t.pendown()
#
# draw(11, 5)
#
# t.done()


# Задача 3.
# Створити клас Detail, з полями назва та вартість.
#  Реалізувати додавання екземплярів класу Detail (по типу: detail_1 + detail_2) з допомогою __add__(), результат – сума вартостей товарів. Виконувати перевірку, щоб обидва доданки були типу Detail, в іншому випадку – видавати виключення TypeError.


class Detail:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other, Detail):
            return self.price + other.price
        else:
            raise TypeError({TypeError})


# class Detail_2:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __add__(self, other):
#         if isinstance(other, Detail_2):
#             return self.price + other.price
#         else:
#             raise TypeError({TypeError})


detail_1 = Detail('Key', 500)
detail_2 = Detail('Screw', 20)
# detail_3 = Detail_2('Screw', 20)

total = detail_1 + detail_2
# total_2 = detail_1 + detail_3
print(total)

print('\n')


# 4

class Client:
    def __init__(self, full_name, date_of_birth: str):
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def client_data(self):
        return print(f'Client name: {self.full_name}\nClient DOB: {self.date_of_birth}')


class Account:
    def __init__(self, client: Client):
        self.client = client
        self._account_balance = 0

    def _change_account_balance(self, amount):
        self._account_balance += amount


class GoldAccount(Account):
    def __display_account_balance(self):
        print(f"Account balance: {self._account_balance}")

    def __change_account_balance(self, amount):
        self._account_balance += amount

    def change_account_balance(self, amount):
        self._change_account_balance(amount)
