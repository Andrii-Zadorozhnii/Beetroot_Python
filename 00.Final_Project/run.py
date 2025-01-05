from config import TOKEN  # Импортируем токен для бота из файла config
import asyncio
import logging

# Создаем объект бота с использованием токена
bot = Bot(token=TOKEN)

# Создаем диспетчер для обработки событий
dp = Dispatcher()


# Основная функция запуска бота
async def main():
    # Запуск поллинга (бот начинает слушать обновления)
    await dp.start_polling(bot)


# Если файл запускается напрямую, запускаем бота
if __name__ == '__main__':
    # Включаем логирование для отображения информации в терминале
    logging.basicConfig(level=logging.INFO)
    try:
        # Запуск асинхронного события
        asyncio.run(main())
    except KeyboardInterrupt:
        # Обрабатываем завершение работы через Ctrl+C
        print('Exit')
