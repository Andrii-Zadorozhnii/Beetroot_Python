from config import TOKEN  # Импортируем токен для бота из файла config

# Создаем объект бота с использованием токена
bot = Bot(token=TOKEN)

# Создаем диспетчер для обработки событий
dp = Dispatcher()
