import asyncio
import asyncpg
import hashlib
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# 🔹 Конфигурация
TOKEN = "7671224104:AAGO1E0ssPTXjko_Ji7n3w0l3S8B52EeWzQ"

DB_CONFIG = {
    "user": "postgres",
    "password": "postgres",
    "database": "cargo_db",
    "host": "localhost"
}

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}  # Временное хранилище данных
def run_bot():
    print("Bot is running")

def generate_unique_id(data: dict) -> str:
    """Генерирует уникальный номер перевозки на основе введенных данных."""
    raw_data = f"{data['name']}{data['origin']}{data['destination']}{data['company']}{data['phone']}{data['payment']}"
    return hashlib.sha256(raw_data.encode()).hexdigest()[:10]  # Берем первые 10 символов хэша

@dp.message(Command("start"))
async def start(message: Message):
    """Запуск бота"""
    user_data[message.chat.id] = {}  # Создаем временное хранилище
    await message.answer("Введите название груза:")

@dp.message()
async def collect_data(message: Message):
    """Сбор данных о перевозке по шагам"""
    user_id = message.chat.id
    user_input = message.text

    if "name" not in user_data[user_id]:
        user_data[user_id]["name"] = user_input
        await message.answer("Введите пункт отправления:")
    elif "origin" not in user_data[user_id]:
        user_data[user_id]["origin"] = user_input
        await message.answer("Введите пункт назначения:")
    elif "destination" not in user_data[user_id]:
        user_data[user_id]["destination"] = user_input
        await message.answer("Введите название компании:")
    elif "company" not in user_data[user_id]:
        user_data[user_id]["company"] = user_input
        await message.answer("Введите номер телефона менеджера:")
    elif "phone" not in user_data[user_id]:
        user_data[user_id]["phone"] = user_input
        await message.answer("Введите сумму оплаты (в USD):")
    elif "payment" not in user_data[user_id]:
        try:
            user_data[user_id]["payment"] = float(user_input)  # Преобразуем в число
        except ValueError:
            await message.answer("Ошибка! Введите корректную сумму оплаты (число).")
            return
        await message.answer("Введите ссылку на изображение груза:")
    elif "image" not in user_data[user_id]:
        user_data[user_id]["image"] = user_input
        user_data[user_id]["shipment_id"] = generate_unique_id(user_data[user_id])  # Генерация номера перевозки

        await save_to_db(user_id)
        await message.answer(f"✅ Данные о грузе сохранены в базе!\n📦 Номер перевозки: {user_data[user_id]['shipment_id']}")
        del user_data[user_id]  # Очищаем данные после сохранения

async def save_to_db(user_id: int):
    """Сохранение данных о перевозке в PostgreSQL (таблица cargo_cargo)"""
    conn = await asyncpg.connect(**DB_CONFIG)
    data = user_data[user_id]
    await conn.execute(
        """
        INSERT INTO cargo_cargo (shipment_id, name, origin, destination, company, phone, payment, image) 
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        """,
        data["shipment_id"], data["name"], data["origin"], data["destination"],
        data["company"], data["phone"], data["payment"], data["image"]
    )
    await conn.close()

async def main():
    """Запуск бота"""
    await dp.start_polling(bot)

asyncio.run(main())