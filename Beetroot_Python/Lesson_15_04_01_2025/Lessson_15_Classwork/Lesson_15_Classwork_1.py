import time
from functools import wraps


# 1. Створити просту функцію та пару декораторів (перший декоратор виводить befor та after, другий – виводить час виконання функції) (задати опис як для функції так і для внутрішьної функції)
# - застосувати їх через присвоєння змінній
# - через @
# - через @wraps
# у всіх 3 варіантах вивести (__doc__, __name__)
# 2. Доопрацюйте функцію з задачі 1, щоб їй можна було передавати параметри.
# 3. Застосуйте до функції два декоратори одночасно. Який з них виконується першим ?
# 4. Доопрацювати перший декоратор з задачі 1, щоб можна було задавати кількість повторень befor та after.(3 вкладені функції).


def main_dec(size=2):
    def dec_1(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(
                f'Function name is: {func.__name__}'
            )
            print(
                f'Function docstring: {func.__doc__}'
            )
            for i in range(size):
                print('Before')
            result = func(*args, **kwargs)
            for i in range(size):
                print('After')
            return result

        return wrapper

    return dec_1


@main_dec(size=2)
def simple_f():
    """Simple function"""
    print(
        'Simple function'
    )


@main_dec(size=2)
def time_calculation():
    """Function for time calculation"""

    time.sleep(1)
    start = time.time()

    print(
        'Calculation...3...'
    )
    time.sleep(1)
    print(
        'Calculation...2..'
    )
    time.sleep(1)
    print(
        'Calculation...1.'
    )
    time.sleep(1)

    end = time.time()
    need_time = str((end - start))
    print(
        f'Time need for calculation: {need_time[:5]} sec'
    )


time_calculation()
