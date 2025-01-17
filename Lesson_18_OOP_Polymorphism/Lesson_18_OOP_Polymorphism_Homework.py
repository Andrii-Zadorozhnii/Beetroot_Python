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


class Library:
    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def __str__(self):
        return f'Library: {self.name}, Books: {self.books}, Authors: {self.authors}'

    def __repr__(self):
        return f'Library: {type(self.name)}, Books: {type(self.books)}, Authors: {type(self.authors)}'


class Book:
    total_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __str__(self):
        return f'Book: {self.name}, Year: {self.year}, Author: {self.author}'

    def __repr__(self):
        return f'Book: {type(self.name)}, Year: {type(self.year)}, Author: {type(self.author)}'


print(
    '''
Task 3
Fraction
    '''
)

print(
    '''
Task 4
Method overloading.
    '''
)
