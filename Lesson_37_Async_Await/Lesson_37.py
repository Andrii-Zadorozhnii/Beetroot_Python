import asyncio
import aiohttp
import requests
import time
from functools import wraps

# 1. (IO-Bound)Нам потрібно отримати 3 курса валют з API Нацбанку (припустимо що API за 1 раз повертає лише курс по одній валюті).
# Спробуйте це зробити послідовно, та з використанням asyncio.
# Виміряйте час, для обох випадків (запустіть 3 рази).

#  2. (CPU-bound) Обчислення чисел Фібоначі (з допомогою рекурсії), які займають кілька секунд. Запустіть 3 рази для кількох обчислень, послідовно, та з використанням asyncio.
#  Виміряйте час, для обох випадків.

url_usd = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250304&end=20250305&valcode=usd&sort=exchangedate&order=desc&json'
url_eur = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250304&end=20250305&valcode=eur&sort=exchangedate&order=desc&json'
url_aud = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250304&end=20250305&valcode=aud&sort=exchangedate&order=desc&json'


def web_pars(url):
    result = requests.get(url).json()
    print(f'1 {result[0]['enname']}:{result[0]['rate']:.2f} UAH')


def parsing_3():
    start_time = time.time()
    web_pars(url_usd)
    web_pars(url_eur)
    web_pars(url_aud)

    need_time = time.time() - start_time
    print(f'\nNeed time for calculation: {need_time:.2f} second')


parsing_3()

print('\n Async')


async def async_pars(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f'1 {data[0]['enname']}:{data[0]['rate']:.2f} UAH')

            # print(data)


async def main():
    start_time = time.time()
    value1 = asyncio.create_task(async_pars(url_usd))
    value2 = asyncio.create_task(async_pars(url_eur))
    value3 = asyncio.create_task(async_pars(url_aud))

    await asyncio.gather(value1, value2, value3, )

    need_time = time.time() - start_time
    print(f'\nNeed time for calculation: {need_time:.2f} second')


asyncio.run(main())

print('Fibonacci')


def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\nВремя выполнения: {end - start:.2f} секунд")
        return result

    return wrapper


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@time_counter
def sequential_fibonacci():
    results = [fibonacci(35) for _ in range(3)]
    print("Result:", results)


def async_time_counter(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\nВремя выполнения: {end - start:.2f} секунд")
        return result

    return wrapper


async def fibonacci_async(n: int) -> int:
    return await asyncio.to_thread(fibonacci, n)


@async_time_counter
async def sequential_fibonacci_async():
    tasks = [fibonacci_async(35) for _ in range(3)]
    results = await asyncio.gather(*tasks)
    print("Результаты:", results)


print("\nСинхронное вычисление Фибоначчи:")
sequential_fibonacci()

print("\nАсинхронное вычисление Фибоначчи:")
asyncio.run(sequential_fibonacci_async())
