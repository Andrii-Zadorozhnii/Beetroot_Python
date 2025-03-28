# Вот список из 20 задач, начиная с самых простых и заканчивая более сложными. Каждое задание поможет тебе постепенно углубить знания об async и await.
#
from aiohttp import ClientSession

print(
    '\n1. Простая асинхронная функция. Напиши асинхронную функцию, которая просто выводит “Hello, world!” и ждет 1 секунду перед завершением.')

import asyncio


async def print_something(some_text: str, delay: int) -> None:
    print(some_text)
    await asyncio.sleep(1)
    print(f'Delayed {delay} second. Completed')


asyncio.run(print_something('Hello', 4))

print(
    '\n2. Асинхронная задержка. Напиши программу, которая вызывает асинхронную функцию с задержкой в 2 секунды, а затем выводит сообщение Task Complete.')

import asyncio


async def delay(delay_time: int) -> None:
    await asyncio.sleep(delay_time)
    print('Task Complete')


asyncio.run(delay(4))

print(
    '\n3. Запуск нескольких асинхронных задач. Создай 3 асинхронные задачи, каждая из которых выполняет задержку на 1, 2 и 3 секунды. Выведи их результаты.')


async def task_1():
    print('task_1')
    await asyncio.sleep(1)


async def task_2():
    print('task_2')
    await asyncio.sleep(2)


async def task_3():
    print('task_3')
    await asyncio.sleep(3)


async def main():
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())
    task3 = asyncio.create_task(task_3())

    await task1, task2, task3


asyncio.run(main())

print(
    '\n4. Асинхронная запись в файл. Напиши асинхронную функцию, которая записывает строку в файл с задержкой в 1 секунду.')

import asyncio
import aiofiles


async def write_in_file(some_text: str) -> None:
    async with aiofiles.open('task_4_file', 'w') as file:
        await asyncio.sleep(1)
        await file.write(some_text)


asyncio.run(write_in_file('Hello asyncio'))

print('\n5. Загрузка нескольких веб-страниц с aiohttp. '
      'Напиши программу, которая загружает 2 веб-страницы с использованием aiohttp асинхронно и выводит их заголовки.')

import asyncio
import aiohttp


async def load_website(url: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
        # print(data)


asyncio.run(load_website('https://linkedin.com'))

print(
    '\n6. Ожидание нескольких задач с asyncio.gather. Создай три асинхронные функции, каждая с разной задержкой, и дождись их завершения с помощью asyncio.gather.')

import asyncio


async def task_6_func(number: int) -> None:
    if number == 2:
        raise ValueError
    else:
        print(f'number{number}')


async def main_6() -> None:
    results = await asyncio.gather(
        task_6_func(1),
        task_6_func(2),
        task_6_func(3),
        return_exceptions=True,
    )


asyncio.run(main_6())

print(
    '\n7. Асинхронный запрос с обработкой ошибок. Реализуй асинхронный запрос с использованием aiohttp и обработкой исключений, выводя сообщение об ошибке, если запрос не удался.')

import asyncio
import aiohttp


async def https_request(url: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:

                print('Response status code 200. Well done')
            else:
                raise Exception(f' Error code: {response.status}')


asyncio.run(https_request('https://google.com'))

print(
    '\n8. Параллельная загрузка данных с использованием asyncio.gather. Загрузите данные с 3 различных веб-страниц параллельно, используя asyncio.gather.')

import asyncio
import aiofiles
import aiohttp
import time

web_sites = [
    'https://google.com',
    'https://github.com',
    'https://linkedin.com'
]


async def get_website(url: str) -> None:
    """
    Асинхронная функция для получения данных с веб-сайта.
    Использует aiohttp для выполнения асинхронного запроса.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.text()

                else:
                    print(f"Ошибка {response.status} при запросе {url}")
        except Exception as e:
            print(f"Ошибка при запросе {url}: {e}")


async def main_8() -> None:
    """
    Основная асинхронная функция для запуска всех задач одновременно.
    """
    print(f'Start time: {time.strftime("%Y-%m-%d %H:%M:%S")}')

    tasks = [asyncio.create_task(get_website(url)) for url in web_sites]
    await asyncio.gather(*tasks)

    print(f'End time: {time.strftime("%Y-%m-%d %H:%M:%S")}')


asyncio.run(main_8())

print(
    '\n9. Асинхронная очередь задач. Создайте очередь задач с помощью asyncio.Queue и выполняйте задачи асинхронно, передавая их через очередь.')

import asyncio

print(
    '\n10. Асинхронный парсинг данных. Напиши асинхронную программу, которая загружает страницы с несколькими сайтами и парсит их содержимое (например, находит все заголовки).')

import asyncio

print(
    '\n11. Параллельная запись в файл. Напиши программу, которая асинхронно записывает данные с разных сайтов в разные части одного файла.')

import asyncio

print(
    '\n12. Ожидание с таймаутом. Напиши функцию, которая выполняет асинхронный запрос с таймаутом на 3 секунды. Если запрос не завершится вовремя, он должен быть отменен.')

import asyncio

print('\n13. Асинхронная обработка с использованием asyncio.create_task. '
      'Создай несколько асинхронных задач с помощью asyncio.create_task, которые выполняют различные действия с задержками, и отслеживай их результаты.')

import asyncio

print('\n14. Асинхронные задачи с зависимостью. '
      'Напиши две асинхронные функции, где вторая зависит от результата первой (например, получение данных с одного сайта перед загрузкой другого).')

import asyncio

print('\n15. Асинхронная загрузка больших файлов. '
      'Напиши асинхронную программу, которая скачивает большие файлы по частям, используя aiohttp и async for.')

import asyncio

print('\n16. Асинхронная обработка задач с результатами. '
      'Напиши программу, которая выполняет несколько асинхронных запросов и обрабатывает их результаты после завершения всех задач.')

import asyncio

print('\n17. Асинхронный таймер. '
      'Реализуй асинхронный таймер, который выполняет задачу каждую секунду в течение 10 секунд.')

import asyncio

print('\n18. Реализация асинхронного сервера. '
      'Напиши простой асинхронный HTTP-сервер с использованием aiohttp, который принимает запросы и отвечает текстом.')

import asyncio

print('\n19. Асинхронная обработка нескольких файлов. '
      'Напиши программу, которая асинхронно читает несколько больших файлов и обрабатывает их содержимое, например, подсчитывает количество строк в каждом.')

import asyncio

print('\n20. Асинхронная работа с базой данных. '
      'Напиши программу, которая асинхронно взаимодействует с базой данных (например, SQLite или PostgreSQL), выполняет несколько запросов и обрабатывает результаты.')
import asyncio
