print(
    '''
Task 1
Method overloading.
    '''
)


class Animal:

    def talk(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):

    def talk(self):
        return print('Dog making: woof woof')


class Cat(Animal):

    def talk(self):
        return print('Cat doing: meow meow')


def make_talk(animal: Animal):
    if isinstance(animal, Animal):
        animal.talk()
    else:
        print("This is not an Animal instance.")


dog = Dog()
cat = Cat()

dog.talk()
cat.talk()

make_talk(dog)
make_talk(cat)

print(
    '''
Task 2
Library
    '''
)


#
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}'

    def __repr__(self):
        return f'Author: {type(self.name)}, Country: {type(self.country)}, Birthday: {type(self.birthday)}'


class Book:
    total_books = []

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books.append(self)
        print(
            f'Total Books is: {len(Book.total_books)}'
        )

    def __str__(self):
        return f'Book: {self.name}, Year: {self.year}, Author: {self.author}'

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

    # def book_data(self):
    #     return print(f'{self.name},{self.year},{self.author.name},{self.author.books}')


class Library:
    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        print(f'{book} added to the library.')
        return book

    def group_by_author(self, author: Author):
        books_by_author = [book for book in self.books if book.author == author]
        print(f'Books by {author.name}: {books_by_author}')
        return books_by_author

    def group_by_year(self, year: int):
        books_by_year = [book for book in self.books if book.year == year]
        print(f'Books from year {year}: {books_by_year}')
        return books_by_year

    def __str__(self):
        return f'Library: {self.name}, Books: {self.books}, Authors: {self.authors}'

    def __repr__(self):
        return f'Library: {type(self.name)}, Books: {type(self.books)}, Authors: {type(self.authors)}'


author_1 = Author('Igor', 'Ukraine', '27.06.1978')
print(author_1)

library = Library("Central Library")
book_1 = library.new_book('Book One', 1992, author_1)
book_2 = library.new_book('Book Two', 1993, author_1)

books_by_author = library.group_by_author(author_1)
books_by_year = library.group_by_year(1992)

print("All books in the library:")
print(library.books)

print(
    '''
Task 3
Fraction
    '''
)

# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
# Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction
from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):

        divisor = gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

    def __add__(self, other):

        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction.")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):

        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction.")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):

        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction.")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):

        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction.")
        if other.numerator == 0:
            raise ZeroDivisionError("Деление на дробь с нулевым числителем.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):

        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):

        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):

        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):

        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):

        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __ne__(self, other):

        return not self.__eq__(other)

    def __str__(self):

        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    print(x)  # 1/2
    y = Fraction(1, 4)
    print(y)  # 1/4

    z = x + y
    print(z)  # 3/4

    w = x - y
    print(w)  # 1/4

    u = x * y
    print(u)  # 1/8

    v = x / y
    print(v)  # 2

    e = Fraction(3, 4)
    print(z == e)
    print(z != e)
    print(x < y)
    print(x > y)
    print(x <= y)
    print(x >= y)
