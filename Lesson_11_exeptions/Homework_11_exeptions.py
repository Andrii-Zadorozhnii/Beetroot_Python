# Task 1
#
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?


def oops():
    raise IndexError("Это ошибка IndexError!")

def handle_oops():
    try:
        oops()
    except IndexError:
        print(f"Исключение перехвачено: {IndexError}")
    except KeyError:
        print(f"Исключение KeyError перехвачено: {KeyError}")

handle_oops()


# Task 2
#
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which catches an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def calculate_square():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        result = (a ** 2) / b
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введенные значения должны быть числами.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
    except Exception:
        print(f"Неизвестная ошибка: {Exception}")

# Тестируем
calculate_square()