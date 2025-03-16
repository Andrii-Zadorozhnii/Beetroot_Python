import asyncio
import asyncpg
import hashlib
import re
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import logging

from cargo_project.settings import BOT_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔐 Конфигурационные параметры
TOKEN = BOT_TOKEN  # Токен вашего телеграм-бота
DB_CONFIG = {  # Параметры подключения к PostgreSQL
    "user": "postgres",
    "password": "postgres",
    "database": "cargo_db",
    "host": "localhost"
}

# Соль для хеширования (должна быть уникальной и храниться в безопасном месте)
SALT = "your_unique_salt_value"

# 🏗️ Инициализация основных компонентов бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 📦 Хранилище временных данных пользователя во время операций
user_data = {}

# 🔄 Соответствие кнопок интерфейса полям базы данных
FIELD_MAPPING = {
    "📦 Название": "name",
    "🚛 Отправление": "origin",
    "📍 Назначение": "destination",
    "🏢 Компания": "company",
    "📞 Телефон": "phone",
    "💰 Оплата": "payment",
    "🖼 Изображение": "image",
    "📝 Комментарий": "description"
}

# 🎛️ Главное меню с основными действиями
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить груз"), KeyboardButton(text="✏ Изменить груз")],
        [KeyboardButton(text="🗑 Удалить груз"), KeyboardButton(text="👀 Мои грузы")]
    ],
    resize_keyboard=True  # Автоматический размер кнопок
)

# 🖍️ Меню выбора полей для редактирования
edit_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Название"), KeyboardButton(text="🚛 Отправление")],
        [KeyboardButton(text="📍 Назначение"), KeyboardButton(text="🏢 Компания")],
        [KeyboardButton(text="📞 Телефон"), KeyboardButton(text="💰 Оплата")],
        [KeyboardButton(text="🖼 Изображение"), KeyboardButton(text="📝 Комментарий")],
        [KeyboardButton(text="🔙 Назад")]  # Кнопка возврата в главное меню
    ],
    resize_keyboard=True
)

# ✅❌ Меню подтверждения действий
confirm_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Да"), KeyboardButton(text="❌ Нет")]
    ],
    resize_keyboard=True
)


def hash_data(data: str) -> str:
    """
    Хеширует данные с использованием SHA-256 и соли.
    Возвращает строку из 64 символов (хеш).
    """
    return hashlib.sha256((data + SALT).encode()).hexdigest()


def generate_unique_id(data: dict) -> str:
    """
    Генерирует уникальный идентификатор перевозки на основе хеша данных.
    Использует SHA-256 для создания 10-символьного хеша.
    """
    raw_data = f"{data['name']}{data['origin']}{data['destination']}{data['company']}{data['phone']}{data['payment']}"
    return hash_data(raw_data)[:10]


async def get_cargo_by_id(shipment_id: str, user_id: int) -> dict:
    """
    Получает данные о грузе по его идентификатору и идентификатору пользователя.
    Если груз не найден или не принадлежит пользователю, выбрасывает исключение.
    """
    try:
        conn = await asyncpg.connect(**DB_CONFIG)
        cargo = await conn.fetchrow(
            """
            SELECT * FROM cargo_cargo 
            WHERE shipment_id = $1 AND user_id = $2
            """,
            shipment_id, hash_data(str(user_id))  # Хешируем user_id
        )
        await conn.close()

        if not cargo:
            logger.warning(f"Груз не найден: shipment_id={shipment_id}, user_id={hash_data(str(user_id))}")
            raise ValueError("Груз не найден или у вас нет прав доступа.")

        return dict(cargo)  # Конвертация в словарь
    except Exception as e:
        logger.error(f"Ошибка при получении груза: {e}")
        raise


async def validate_phone(phone: str) -> bool:
    """Проверка корректности номера телефона"""
    phone_pattern = re.compile(r"^\+?[1-9]\d{1,14}$")
    return bool(phone_pattern.match(phone))


async def validate_payment(payment: str) -> bool:
    """Проверка корректности суммы оплаты"""
    try:
        amount = float(payment)
        return amount > 0
    except ValueError:
        return False


async def validate_name(name: str) -> bool:
    """Проверка корректности названия груза"""
    return 2 <= len(name) <= 100


async def validate_company(company: str) -> bool:
    """Проверка корректности названия компании"""
    return 2 <= len(company) <= 100


async def validate_description(description: str) -> bool:
    """Проверка корректности комментария"""
    return len(description) <= 500


@dp.message(Command("start"))
async def start(message: Message):
    """Обработчик команды /start - начальная точка взаимодействия с ботом"""
    await message.answer("👋 Привет! Выберите действие:", reply_markup=main_menu)


@dp.message(lambda message: message.text == "👀 Мои грузы")
async def show_all_cargos(message: Message):
    """Отображение всех грузов пользователя в форматированном виде"""
    user_id = message.chat.id
    logger.info(f"Пользователь {user_id} запросил список грузов.")

    # Получаем грузы для текущего пользователя
    cargos = await get_user_cargos(user_id)

    if not cargos:
        await message.answer("У вас нет сохраненных грузов.")
        return

    # Формируем ответ
    response = "📦 Список ваших грузов:\n\n"
    for cargo in cargos:
        response += f"🔸 Номер перевозки: {cargo['shipment_id']}\n"
        response += f"📦 Название: {cargo['name']}\n"
        response += f"🚚 Маршрут: {cargo['origin']} → {cargo['destination']}\n"
        response += f"🏢 Компания: {cargo['company']}\n"
        response += f"💵 Оплата: {cargo['payment']}\n\n"
        response += "━" * 20 + "\n\n"

    await message.answer(response, reply_markup=main_menu)


async def get_user_cargos(user_id: int) -> list:
    """Получение списка всех грузов пользователя из базы данных"""
    conn = await asyncpg.connect(**DB_CONFIG)
    cargos = await conn.fetch(
        "SELECT * FROM cargo_cargo WHERE user_id = $1",
        hash_data(str(user_id))  # Хешируем user_id и передаем как строку
    )
    await conn.close()
    return [dict(cargo) for cargo in cargos]


@dp.message()
async def handle_user_input(message: Message):
    """Главный обработчик сообщений, распределяющий действия"""
    user_id = message.chat.id
    text = message.text

    # 🎮 Обработка основных команд главного меню
    if text == "➕ Добавить груз":
        user_data[user_id] = {"state": "adding", "data": {}}
        await message.answer("Введите название груза:")
    elif text == "✏ Изменить груз":
        user_data[user_id] = {"state": "editing", "data": {}}
        await message.answer("Введите номер перевозки для редактирования:")
    elif text == "🗑 Удалить груз":
        user_data[user_id] = {"state": "deleting", "data": {}}
        await message.answer("Введите номер перевозки для удаления:")

    # 🛠️ Обработка состояний пользователя
    elif user_id in user_data:
        if user_data[user_id]["state"] == "adding":
            await process_cargo_data(message)
        elif user_data[user_id]["state"] == "editing":
            await process_edit_cargo(message)
        elif user_data[user_id]["state"] == "deleting":
            await process_delete_cargo(message)
    else:
        await message.answer("Используйте кнопки для работы с ботом.")


async def process_cargo_data(message: Message):
    """Пошаговая обработка данных нового груза"""
    user_id = message.chat.id
    text = message.text
    current_data = user_data[user_id]["data"]

    if "name" not in current_data:
        if await validate_name(text):
            current_data["name"] = text
            await message.answer("Введите пункт отправления (город):")
        else:
            await message.answer("Название груза должно быть от 2 до 100 символов. Попробуйте еще раз.")
    elif "origin" not in current_data:
        current_data["origin"] = text
        await message.answer("Введите пункт назначения (город):")
    elif "destination" not in current_data:
        current_data["destination"] = text
        await message.answer("Введите название компании:")
    elif "company" not in current_data:
        if await validate_company(text):
            current_data["company"] = text
            await message.answer("Введите номер телефона менеджера:")
        else:
            await message.answer("Название компании должно быть от 2 до 100 символов. Попробуйте еще раз.")
    elif "phone" not in current_data:
        if await validate_phone(text):
            current_data["phone"] = text
            await message.answer("Введите сумму оплаты (в USD):")
        else:
            await message.answer("Номер телефона должен быть в международном формате. Попробуйте еще раз.")
    elif "payment" not in current_data:
        if await validate_payment(text):
            current_data["payment"] = float(text)
            await message.answer("Введите ссылку на изображение груза:")
        else:
            await message.answer("Сумма оплаты должна быть положительным числом. Попробуйте еще раз.")
    elif "image" not in current_data:
        if text.startswith("http"):
            current_data["image"] = text
            await message.answer("Введите комментарий к грузу:")
        else:
            await message.answer("Ссылка на изображение должна начинаться с 'http'. Попробуйте еще раз.")
    elif "description" not in current_data:
        if await validate_description(text):
            current_data["description"] = text
            current_data["shipment_id"] = generate_unique_id(current_data)
            await save_to_db(user_id)
            await message.answer(f"✅ Груз сохранен!\n{format_cargo_data(current_data)}", reply_markup=main_menu)
            del user_data[user_id]  # Очистка временных данных
        else:
            await message.answer("Комментарий должен быть не более 500 символов. Попробуйте еще раз.")


async def save_to_db(user_id: int):
    """Сохранение данных груза в базу данных"""
    conn = await asyncpg.connect(**DB_CONFIG)
    data = user_data[user_id]["data"]
    await conn.execute(
        """
        INSERT INTO cargo_cargo 
        (shipment_id, name, origin, destination, company, 
         phone, payment, image, description, user_id)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
        """,
        data["shipment_id"], data["name"], data["origin"],
        data["destination"], data["company"], data["phone"],
        data["payment"], data["image"], data["description"],
        hash_data(str(user_id))  # Хешируем user_id и передаем как строку
    )
    await conn.close()


async def process_edit_cargo(message: Message):
    """Обработка процесса редактирования груза"""
    user_id = message.chat.id
    text = message.text
    current_data = user_data[user_id]["data"]

    # 🔄 Логика многошагового редактирования
    if "shipment_id" not in current_data:
        try:
            cargo = await get_cargo_by_id(text, user_id)
            current_data["shipment_id"] = text
            await message.answer("Выберите поле для редактирования:", reply_markup=edit_menu)
        except ValueError as e:
            await message.answer(str(e))
            del user_data[user_id]
    elif "field" not in current_data:
        if text == "🔙 Назад":
            del user_data[user_id]
            await message.answer("👋 Привет! Выберите действие:", reply_markup=main_menu)
        elif text in FIELD_MAPPING:
            current_data["field"] = FIELD_MAPPING[text]
            await message.answer(f"Введите новое значение для {text}:")
        else:
            await message.answer("Неверный выбор поля. Используйте кнопки.")
    elif "new_value" not in current_data:
        current_data["new_value"] = text
        await message.answer(f"Вы уверены, что хотите изменить {text}?",
                             reply_markup=confirm_menu)
    else:
        if text == "✅ Да":
            await update_cargo_in_db(
                current_data["shipment_id"],
                current_data["field"],
                current_data["new_value"],
                user_id
            )
            await message.answer(f"✅ Поле успешно обновлено!", reply_markup=main_menu)
        else:
            await message.answer("Изменение отменено.", reply_markup=main_menu)
        del user_data[user_id]


async def update_cargo_in_db(shipment_id: str, field: str, value: str, user_id: int):
    """Обновление конкретного поля груза в базе данных"""
    allowed_fields = set(FIELD_MAPPING.values())
    if field not in allowed_fields:
        raise ValueError("Недопустимое имя поля")

    conn = await asyncpg.connect(**DB_CONFIG)
    result = await conn.execute(
        f"""
        UPDATE cargo_cargo 
        SET {field} = $1 
        WHERE shipment_id = $2 AND user_id = $3
        """,
        value, shipment_id, hash_data(str(user_id))  # Хешируем user_id
    )
    await conn.close()

    if result == "UPDATE 0":
        raise ValueError("Груз не найден или нет прав доступа")


async def process_delete_cargo(message: Message):
    """Обработка процесса удаления груза"""
    user_id = message.chat.id
    text = message.text
    current_data = user_data[user_id]["data"]

    if "shipment_id" not in current_data:
        try:
            cargo = await get_cargo_by_id(text, user_id)
            current_data["shipment_id"] = text
            await message.answer(f"Вы уверены, что хотите удалить груз с номером {text}?", reply_markup=confirm_menu)
        except ValueError as e:
            await message.answer(str(e))
            del user_data[user_id]
    elif "confirmation" not in current_data:
        if text == "✅ Да":
            await delete_cargo_from_db(current_data["shipment_id"], user_id)
            await message.answer(f"✅ Груз успешно удален!", reply_markup=main_menu)
        else:
            await message.answer("Удаление отменено.", reply_markup=main_menu)
        del user_data[user_id]


async def delete_cargo_from_db(shipment_id: str, user_id: int):
    """Удаление груза из базы данных с проверкой прав доступа"""
    conn = await asyncpg.connect(**DB_CONFIG)
    result = await conn.execute(
        """
        DELETE FROM cargo_cargo 
        WHERE shipment_id = $1 AND user_id = $2
        """,
        shipment_id, hash_data(str(user_id))  # Хешируем user_id
    )
    await conn.close()

    if result == "DELETE 0":
        raise ValueError("Груз не найден или нет прав доступа")


def format_cargo_data(data: dict) -> str:
    """Форматирование данных груза для красивого отображения"""
    return (
        f"📦 Название: {data['name']}\n"
        f"🚛 Отправление: {data['origin']}\n"
        f"📍 Назначение: {data['destination']}\n"
        f"🏢 Компания: {data['company']}\n"
        f"📞 Телефон: {data['phone']}\n"
        f"💰 Оплата: {data['payment']} USD\n"
        f"📝 Комментарий: {data['description']}\n"
        f"🔑 Номер перевозки: {data['shipment_id']}"
    )


async def main():
    """Основная функция запуска бота"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())