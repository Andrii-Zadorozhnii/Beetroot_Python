# Задание 1
#
# Практика асинхронного кода
#
# Создайте отдельный асинхронный код для вычисления чисел Фибоначчи, факториала, квадратов и кубов для входного числа.
# Запланируйте выполнение этого кода с помощью asyncio.gather для списка целых чисел от 1 до 10.
# Вам нужно получить четыре списка результатов из соответствующих функций.
#
# Перепишите код, чтобы использовать простые функции для получения тех же результатов, но с использованием библиотеки многопроцессорной обработки.
# Засеките время выполнения обеих реализаций, исследуйте результаты, какая реализация более эффективна, почему вы получили такой результат.

import time
import asyncio
import multiprocessing

from typing import List, Tuple

numbers = list(range(1, 11))


async def time_calculation(func, *args):
    start_time = time.time()
    result = await func(*args)
    spent_time = time.time() - start_time
    print(f'\nSpent time for Async func: {spent_time:.5f}seconds\n')
    return result


# Async/Await realisation

async def fibonacci_number(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fibonacci_list = [0, 1]
    for _ in range(2, n):
        await asyncio.sleep(0)
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list


async def factorial_number(n: int) -> int:
    if n < 0:
        raise ValueError()
    result = 1

    for i in range(2, n + 1):
        await asyncio.sleep(0)
        result *= i
    return result


async def square_number(n: int) -> int:
    await asyncio.sleep(0)
    return n ** 2


async def cube_number(n: int) -> int:
    await asyncio.sleep(0)
    return n ** 3


async def main():
    fibonacci_task = [fibonacci_number(n) for n in numbers]
    factorial_task = [factorial_number(n) for n in numbers]
    square_task = [square_number(n) for n in numbers]
    cube_task = [cube_number(n) for n in numbers]

    fibonacci_results, factorial_results, square_results, cube_results = await asyncio.gather(
        asyncio.gather(*fibonacci_task),
        asyncio.gather(*factorial_task),
        asyncio.gather(*square_task),
        asyncio.gather(*cube_task)
    )

    print(f'Fibonacci list: {fibonacci_results}')
    print(f'Factorial number: {factorial_results}')
    print(f'Square number: {square_results}')
    print(f'Cube number: {cube_results}')


# Base realization with multiprocessing

def time_calculation_2(func, *args):
    start_time = time.time()
    result = func(*args)
    spent_time = time.time() - start_time
    print(f'\nSpent time for base func: {spent_time:.5f} seconds\n')
    return result


def fibonacci_number_base(n: int) -> List[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibonacci_list = [0, 1]
    for _ in range(2, n):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list


def factorial_number_base(n: int) -> int:
    if n < 0:
        raise ValueError()

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def square_number_base(n: int) -> int:
    return n ** 2


def cube_number_base(n: int) -> int:
    return n ** 3


def main_base():
    with multiprocessing.Pool() as pool:
        (fibonacci_results, factorial_results, square_results, cube_results) = (
            pool.map(fibonacci_number_base, numbers), pool.map(factorial_number_base, numbers),
            pool.map(square_number_base, numbers),
            pool.map(cube_number_base, numbers))

    print(f'Fibonacci numbers: {fibonacci_results}')
    print(f'Factorial numbers: {factorial_results}')
    print(f'Square number: {square_results}')
    print(f'Cube number: {cube_results}')

    return fibonacci_results, factorial_results, square_results, cube_results


# Run Modules
if __name__ == '__main__':
    asyncio.run(time_calculation(main))  # Async

    time_calculation_2(main_base)  # Multiprocessing
