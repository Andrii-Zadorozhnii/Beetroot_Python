from random import randint
from functools import wraps

# Задача 4.
#  Нехай в нас є функція func(), яка повертає кортеж 10-ти цілих чисел в діапазоні 0 до 100.
#  Зробіть декоратор з використанням функції map(). Задекорована функція повинна повертати список чисел, кратний 2 (реалізувати при допомозі lambda).

from random import randint
from functools import wraps, reduce


def filter_even(func):
    @wraps(func)
    def wrap():
        even_numbers = map(lambda x: x if x % 2 == 0 else None, func())
        filter_numbers = filter(lambda x: x is not None, even_numbers)
        return list(filter_numbers)

    return wrap


@filter_even
def func():
    return tuple(randint(0, 100) for _ in range(10))


print(func())


# Задача 5.
# Зробіть декоратор для функції func() з задачі 4, який відфільтровує значення, кратні 3. Використати функцію filter() та lambda.

def filter_by_3(func):
    @wraps(func)
    def wrap():
        filtered_by_3 = map(lambda x: x if x % 3 == 0 else None, func())
        filter_numbers = filter(lambda x: x is not None, filtered_by_3)
        return list(filter_numbers)

    return wrap


@filter_by_3
@filter_even
def func():
    return tuple(randint(0, 100) for _ in range(10))


print(func())


# Задача 6.
# Зробіть декоратор для функції func() з задачі 4, який запускає дану функцію 2 рази, а потім повертає результат при допомозі zip (об“єднує отримані в результаті запусків кортежі).

def double_count(func):
    def wrap():
        result1 = func()
        result2 = func()

        zip_list = list(zip(result1, result2))
        return zip_list

    return wrap


@double_count
def func():
    return tuple(randint(0, 100) for _ in range(10))


print(func())


# Задача 7.
# Зробіть декоратор для функції func() з задачі 4, яка реалізує функцію  reduce().

def reduce_decorator(func):
    @wraps(func)
    def wrap():
        result = func()
        reduced_result = reduce(lambda x, y: x + y, result)
        return reduced_result

    return wrap


@reduce_decorator
def func():
    return tuple(randint(0, 100) for _ in range(10))


print(func())


# Задача 8.
# Для задач 4, 5, 6 реалізуйте декоратор з можливістю задання параметрів:
# кратність для задач 4,5
# та кількість запусків функції func() (кортежів).


def filter_multiple(multiple):
    def decorator(func):
        @wraps(func)
        def wrap():
            result = func()
            filtered_result = list(filter(lambda x: x % multiple == 0, result))
            return filtered_result

        return wrap

    return decorator


def double_run(count):
    def decorator(func):
        @wraps(func)
        def wrap():
            results = [func() for _ in range(count)]  # Запускаємо функцію 'count' разів
            return results

        return wrap

    return decorator


@filter_multiple(multiple=3)
def func(multiple=2):
    return tuple(randint(0, 100) for _ in range(10))


@filter_multiple(multiple=3)
def filter_by_3(multiple=3):
    return tuple(randint(0, 100) for _ in range(10))


@double_run(count=2)
def double_count(count=2):
    return tuple(randint(0, 100) for _ in range(10))


print(func())
print(filter_by_3())
print(double_count())
