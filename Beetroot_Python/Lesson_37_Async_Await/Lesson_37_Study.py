# Async/Await в Python
#
# async и await — это ключевые слова для работы с асинхронным программированием в Python. Они позволяют выполнять операции без блокировки основного потока выполнения.
#
# Основные понятия
# 	1.	Асинхронные функции
# 	•	Объявляются с помощью async def
# 	•	Возвращают coroutine (корутину)
# 	•	Выполняются только после вызова await или через asyncio.run()

# 	2.	Ожидание выполнения
# 	•	await используется внутри async-функции, чтобы дождаться результата другой корутины.
# 	•	Без await корутина не начнет выполняться.

# 	3.	Основные механизмы
# 	•	asyncio.run() — запускает корутину.
# 	•	asyncio.create_task() — создает асинхронную задачу.
# 	•	asyncio.gather() — выполняет несколько задач параллельно.

# Простые примеры

# 1. Базовая асинхронная функция

import asyncio  # Модуль для работы с асинхронным программированием

# async def say_hello() -> None:
#     """
#     Асинхронная функция, которая выводит приветствие,
#     затем делает паузу на 1 секунду и снова выводит сообщение.
#     """
#     print("Привет! Начинаем выполнение асинхронной функции.")
#     await asyncio.sleep(1)  # Асинхронная пауза (не блокирует выполнение других задач)
#     print("Прошла 1 секунда! Завершение функции.")
#
#
# # Запускаем асинхронную функцию через asyncio.run()
# asyncio.run(say_hello())

# Вывод:

# Привет! Начинаем выполнение асинхронной функции.
# Прошла 1 секунда! Завершение функции.

# 2. Запуск нескольких задач

# import asyncio  # Модуль для асинхронного программирования
#
#
# async def task(name: str, delay: int) -> None:
#     """
#     Асинхронная задача, имитирующая выполнение работы с задержкой.
#
#     :param name: Название задачи (для отображения в выводе).
#     :param delay: Время задержки в секундах перед завершением задачи.
#     """
#     print(f"Задача {name} началась.")
#     await asyncio.sleep(delay)  # Ожидание заданное количество секунд (не блокируя другие задачи)
#     print(f"Задача {name} завершена.")
#
#
# async def main() -> None:
#     """
#     Главная асинхронная функция, которая запускает несколько задач параллельно.
#     """
#     print("Запуск всех задач.")
#
#     # Создаем асинхронные задачи с разными задержками
#     task1 = asyncio.create_task(task("A", 2))  # Задача "A" с задержкой 2 секунды
#     task2 = asyncio.create_task(task("B", 1))  # Задача "B" с задержкой 1 секунда
#
#     # Ожидаем завершения всех задач
#     await task1
#     await task2
#
#     print("Все задачи выполнены.")
#
#
# # Запускаем асинхронную программу
# asyncio.run(main())

# Вывод:

# Запуск всех задач.
# Задача A началась.
# Задача B началась.
# Задача B завершена.
# Задача A завершена.
# Все задачи выполнены.


# Практическое задание


# Задание:
# Создай программу, которая:
# 	1.	Загружает три веб-страницы (https://example.com/1, https://example.com/2, https://example.com/3).
# 	2.	Использует asyncio и aiohttp для асинхронной загрузки.
# 	3.	Выводит время выполнения.

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
                    # print(f"Данные с {url[:50]}: {data}...")
                    async with aiofiles.open('data.txt', 'w') as file:
                        await file.write(data)
                else:
                    print(f"Ошибка {response.status} при запросе {url}")
        except Exception as e:
            print(f"Ошибка при запросе {url}: {e}")


async def main() -> None:
    """
    Основная асинхронная функция для запуска всех задач одновременно.
    """
    print(f'Start time: {time.strftime("%Y-%m-%d %H:%M:%S")}')

    tasks = [asyncio.create_task(get_website(url)) for url in web_sites]
    await asyncio.gather(*tasks)

    print(f'End time: {time.strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == '__main__':
    asyncio.run(main())
