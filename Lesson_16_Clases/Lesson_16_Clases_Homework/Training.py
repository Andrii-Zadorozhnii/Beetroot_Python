# Вот несколько заданий, которые можно выполнить без использования наследования:

# 	1.	Создание класса для представления книги:
# Создайте класс Book с атрибутами title, author и year.
# Добавьте методы для отображения информации о книге и изменения года издания.
print('\n__Task_1__\n')

books = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    {
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "year": 1851
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932
    },
    {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "year": 1866
    }
]


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_data(self):
        return f'Book title: {self.title}\nBook Author: {self.author}\nBook issued: {self.year}\n'


for i in books:
    book = Book(i['title'], i['author'], i['year'])
    print(book.book_data())

# 	2.	Класс для учета счета в банке:
# Реализуйте класс BankAccount, который будет хранить информацию о балансе, имени владельца и номере счета.
# Добавьте методы для пополнения счета, снятия средств и отображения текущего баланса.
print('\n__Task_2__\n')


class BankAccount:
    def __init__(self, account_balance=0, account_owner_name=None, account_number=0):
        self.account_balance = account_balance
        self.account_owner_name = account_owner_name
        self.account_number = account_number

    def add_balance(self, add_balance):
        self.account_balance += add_balance
        return print(f'Add: {add_balance} to account number: {self.account_number}')

    def withdraw_balance(self, minus_balance):
        if self.account_balance >= minus_balance:
            self.account_balance -= minus_balance
            print(f'Withdraw: {minus_balance} from account number: {self.account_number}')
        else:
            print(f'You cannot withdraw: {minus_balance}. You have on account: {self.account_balance}')

    def display_balance(self):
        return print(f'Current balance is: {self.account_balance}')


user_1 = BankAccount(0, 'Igor', 32345)
user_1.add_balance(3000)
user_1.withdraw_balance(2500)
user_1.display_balance()
user_1.add_balance(350)
user_1.withdraw_balance(1000)
user_1.display_balance()

# 	3.	Класс для представления времени:
# Напишите класс Time, который будет хранить часы, минуты и секунды.
# Реализуйте методы для добавления времени, перевода времени в строковый формат и сравнения двух объектов времени.
print('\n__Task_3__\n')


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        if self.hours >= 24:
            self.hours = self.hours % 24


# 	4.	Класс для расчета площади и периметра прямоугольника:
# Создайте класс Rectangle, который будет иметь два атрибута: длину и ширину.
# Добавьте методы для вычисления площади и периметра.
print('\n__Task_4__\n')


class Rectangle:
    def __init__(self, lenght, wide):
        self.lenght = lenght
        self.wide = wide

    def square_calculation(self):
        return (f'Square {self.lenght} and {self.wide} is: {self.lenght * self.wide}')


square_1 = Rectangle(2, 3)

print(square_1.square_calculation())

# 	5.	Класс для представления ученика:
# Создайте класс Student с атрибутами name, age и grades (список оценок).
# Добавьте методы для добавления оценок, вычисления среднего балла и отображения информации об ученике.
print('\n__Task_5__\n')


class Student:
    def __init__(self, name="name", age=0, grades=list):
        self.name = name
        self.age = age
        self.grades = grades

    def student_data(self):
        a = f'Student name: {self.name}\nStudent age: {self.age}\nStudent grades: {self.grades}'
        return print(a)

    def add_grade(self, grade):
        self.grades.append(grade)
        return print(f'Grades updated.\nUpdated list: {self.grades}')


student_1 = Student('Igor', 22, [2, 3, 4])

student_1.student_data()
student_1.add_grade(5)

# 	6.	Класс для представления треугольника:
# Создайте класс Triangle, который будет хранить три стороны треугольника.
# Реализуйте методы для вычисления периметра и площади треугольника (по формуле Герона).
print('\n__Task_6__\n')


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def perimeter_calculation(self):
        s = (self.side_1 + self.side_2 + self.side_3)
        print(f'Perimeter is: {s}')
        return s

    def area(self):
        s = (self.side_1 + self.side_2 + self.side_3)
        formula_gerona = (s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3)) ** 0.5
        print(f'Area is: {formula_gerona:.2f}')
        return formula_gerona


triangle_1 = Triangle(2, 3, 4)
triangle_1.area()
triangle_1.perimeter_calculation()

# 	7.	Класс для работы с книгами в библиотеке:
# Напишите класс Library, который будет содержать список книг.
# Реализуйте методы для добавления книги в библиотеку, поиска книги по автору или названию и удаления книги.
print('\n__Task_7__\n')


class Library:
    def __init__(self, book_title, book_author, book_year, books=list):
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year
        self.books = books

    def add_book(self):
        new_book = f"{{'title':'{self.book_title}','author':'{self.book_author}','year':{self.book_year}}}"
        self.books.append(new_book)
        print(self.books)


book_1 = Library('Hero', 'Mr.Hero', 2025, books)

book_1.add_book()
