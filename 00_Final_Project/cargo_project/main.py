import asyncio
import subprocess
import os
import sys



# Функция для запуска Django-сервера
async def run_django_server():
    print("Запуск Django-сервера...")
    process = subprocess.Popen([sys.executable, 'manage.py', 'runserver'], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # Важно, чтобы сервер продолжал работать в фоне
    await asyncio.to_thread(process.communicate)
    if process.returncode != 0:
        print(f"Ошибка при запуске Django-сервера: {sys.stderr.decode()}")
    else:
        print(f"Django-сервер запущен.")


# Функция для запуска бота
async def run_bot():
    print("Запуск бота...")
    process = subprocess.Popen([sys.executable, 'runbot.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    await asyncio.to_thread(process.communicate)

    if process.returncode != 0:
        print(f"Ошибка при запуске бота: {sys.stderr.decode()}")
    else:
        print(f"Бот запущен.")


# Главная асинхронная функция для запуска серверов параллельно
async def main():
    print("Запуск серверов...")
    await asyncio.gather(run_django_server(), run_bot())


# Запускаем main, если скрипт выполняется напрямую
if __name__ == "__main__":
    asyncio.run(main())