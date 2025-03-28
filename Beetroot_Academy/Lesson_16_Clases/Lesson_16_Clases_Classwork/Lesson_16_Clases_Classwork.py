print(
    'Lesson 16. Classes Classwork'
)


# 1. Робота з клієнтами:
# Створити клас для клієнта банку, з атрибутами екземпляра:
# Прізвище
# Ім“я
# По-батькові
# вік
# середня зарплата
# місце проживання
# поточна заборгованість
# Останні 2 параметри задайте «Київ» та 0, по замовчуванню.
# Додайте методи:
# для зміни заробітної плати
# для зміни заборгованості
# Додайте атрибут класу «загальна к-сть клієнтів» = 0, збільшуйте його на 1 при створенні екземпляра клієнта
# Створіть методи для :
# друку  атрибуту «загальна к-сть клієнтів»,
# друку типу кожного екземпляру, адреси в пам“яті,
# порівняння екземпляра класу з іншим (один екземпляр рівний іншому, якщо всі їхні значення атрибутів однакові)
# Створіть кілька клієнтів, та перевірте роботу всіх раніше створених методів на одному з них.

class Bank_Client:
    client_counter = 0

    def __init__(self,
                 client_name,
                 client_family_name,
                 client_second_name,
                 client_age,
                 client_average_salary=0,
                 client_living='Kiev',
                 client_credit=0):
        self.client_name = client_name
        self.client_family_name = client_family_name
        self.client_second_name = client_second_name
        self.client_age = client_age
        self.client_average_salary = client_average_salary
        self.client_living = client_living
        self.client_credit = client_credit
        Bank_Client.client_counter += 1
        # print(self.client_counter)
        print(self)

    def __eq__(self, other):
        if isinstance(other, Bank_Client):
            return (
                    self.client_name == other.client_name and
                    self.client_family_name == other.client_family_name and
                    self.client_second_name == other.client_second_name and
                    self.client_age == other.client_age and
                    self.client_average_salary == other.client_average_salary and
                    self.client_living == other.client_living and
                    self.client_credit == other.client_credit
            )
        return False

    def new_salary(self, change_salary):
        print(
            f'Old salary is: {self.client_average_salary}'
        )
        self.client_average_salary = change_salary
        print(
            f'New salary is: {self.client_average_salary}\n'
        )
        return self.client_average_salary

    def new_credit(self, change_credit):
        print(
            f'Old credit score is: {self.client_credit}'
        )
        self.client_credit = change_credit
        print(
            f'New credit score is: {self.client_credit}\n'
        )
        return self.client_credit

    def total_client(self):
        return f'Total Clients is: {Bank_Client.client_counter}\n'


client_1 = Bank_Client('Igor', ' Popov', 'Grinchenko', 32, 500)
client_2 = Bank_Client('Nataly', ' Sviridova', 'Igorevna', 33, 2000)
client_3 = Bank_Client('Igor', ' Popov', 'Grinchenko', 32, 500)
client_4 = Bank_Client('Igor', ' Popov', 'Grinchenko', 32, 500)

client_1.new_salary(3000)
client_1.new_credit(2000)

print(client_1.total_client())
print(client_2.total_client())

# print('Same account') if client_1 == client_2 else print('Dont same')
# print('Same account') if client_3 == client_4 else print('Dont same')

print(client_1 == client_2)
print(client_3 == client_4)


# 2. Банки
# Створіть клас для опису банків з атрибутами екземпляра (інстанса):
# Назва банку (bank_name)
# Додайте атрибут класу number_branches = 100000
# Створіть 2 екземпляра банків, виведіть атрибути
# Виведіть атрибути кожного екземпляру (bank_name, number_branches)
# Додайте атрибут екземпляра number_branches для 1-го банку динамічно (в коді, не в описі класу) number_branches= 100
# З допомогою відповідного методу виведіть атрибути кожного екземпляру (bank_name, number_branches).
# Зрозуміло, чому для одного банку number_branches = 100, а для іншого 100000 ?


class Bank:
    number_branches = 10000

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def new_branches(self, new_value):
        Bank.number_branches = new_value
        return f'New branches is: {Bank.number_branches}\n'

    def all_data(self):
        print(
            f'Bank name : {self.bank_name}\nBank branches: {Bank.number_branches}\n'
        )


bank_1 = Bank('Privat')
bank_2 = Bank('Pivdenny')

print(bank_1.bank_name)
print(bank_1.number_branches)
print(bank_2.bank_name)
print(bank_2.number_branches)

print(bank_1.new_branches(100))

bank_1.all_data()
bank_2.all_data()

# 3. Namespace 1
# Створіть модуль, в якому визначте функцію print(parametr), яка при її виклику буде друкувати „Hello ! I“m function print from {назва модуля}“ + parametr
# Імпортуйте функцію print в головну програму таким чином, щоб перезаписати вбудовний print
# викличіть функцію print
# в головній програмі задайте функцію print(parametr), яка при її виклику буде друкувати „Hello ! I“m function print from {назва модуля}“ + parametr
# викличіть функцію print
# p.s. На цьому прикладі має стати зрозуміло перезапис імен в межах одного простору імен та порядок пошуку імені в просторах імен.

import main.main
import sys

from main.main import print

# print = PR
# hello = 'hello'
# print('1')

# 4. Namespace 2
# В програмі, в просторі імен global задайте змінну universal_var = 0.
# Створіть функцію з вкладеною функцією
# У зовнішній функції задайте змінну universal_var = 1 та виведіть через print її значення (при виводі зазначайте простір імен).
# У внутрішній функції задайте змінну universal_var = 2 та виведіть через print її значення (при виводі зазначайте простір імен).
# Викличте зазначені функції,та виведіть через print значення universal_var з головної програми (при виводі зазначайте простір імен). Зрозуміло чому universal_var відрізняється щоразу ?
# Поекспериментуйте з глобальною змінною universal_var у функціях (слідкуйте за результатами всіх 3 print), з використанням ключового слова global:
# додайте global у зовнішню функцію, поміняйте значення
# (закоментуйте global у зовнішній функції) додайте global у внутрішню функцію, поміняйте значення
# розкоментуйте global у зовнішній функції
# закоментуйте global в функціях, спробуйте universal_var +=1 у зовнішній та внутрішній функціях ? Викинуло виключення, чому ? А якщо повернути global ?
#  робота з ключовим словом nonlocal:
# додайте func_var = 0 на рівні зовнішньої функції, запрінтуйте її (при виводі зазначайте простір імен).
# На рівні внутрішньої функції додайте func_var = 2 запрінтуйте її (при виводі зазначайте простір імен).
# Закоментуйте код з попереднього завдання, на рівні внутрішньої функції додайте nonlocal, виведіть значення func_var
# закоментуйте nonlocal, спробуйте операцію func_var+=1 Викинуло виключення, чому ? А якщо повернути nonlocal ?

universal_var = 0
print(f'Global: {universal_var}')


def func():
    global universal_var
    universal_var += 1
    print(f'Enclosed: {universal_var}')
    func_var = 0
    print(
        f'Func var1 :{func_var}'
    )

    def func_2():
        global universal_var
        # universal_var = 2
        universal_var += 1
        print(f'Local: {universal_var}')
        # func_var = 2
        # print(f'local: {func_var}')
        # func_var = 2
        # nonlocal func_var
        # func_var += 1
        print(
            f'Func var2 :{func_var}'
        )

    func_2()


func()

# 5. Namespace 3.
# Якщо створити 3 вкладені функції, як буде себе вести nonlocal ? До якого рівня буде відноситись ? А global ?

x = 0  # Глобальна змінна x


def f_1():
    x = 10  # Локальна змінна x в f_1
    print(f'Leve_1 {x}')  # Виводиться x з f_1, тобто 10

    def f_2():
        # Змінної x в f_2 немає, тому вона звертається до x з f_1
        print(f'Leve_2 {x}')  # Виводиться x з f_1, тобто 10

        def f_3():
            nonlocal x  # Використовуємо nonlocal для зміни x з f_2 (яке належить f_1)
            x += 1  # Збільшуємо x на 1. Тепер x буде 11 (в f_2, що відноситься до f_1)
            print(f'Leve_3 {x}')  # Виводиться x з f_1 після зміни, тобто 11

        f_3()  # Викликаємо f_3(), яка змінює x

    f_2()  # Викликаємо f_2()


f_1()  # Викликаємо f_1()
