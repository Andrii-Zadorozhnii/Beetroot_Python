import asyncio
import asyncpg
import hashlib
import re
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest, TelegramAPIError
from aiogram.filters import Command
import logging
from cargo_project.settings import BOT_TOKEN, DRIVERS_GROUP_ID, SALT

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Конфигурационные параметры
TOKEN = BOT_TOKEN
DB_CONFIG = {
    "user": "postgres",
    "password": "postgres",
    "database": "cargo_db",
    "host": "localhost"
}

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хранилище временных данных
user_data = {}

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить груз")],
        [KeyboardButton(text="👀 Мои грузы")]
    ],
    resize_keyboard=True
)

# Меню подтверждения действий
confirm_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Да"), KeyboardButton(text="❌ Нет")]
    ],
    resize_keyboard=True
)

# Меню редактирования
edit_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Название"), KeyboardButton(text="🚛 Отправление")],
        [KeyboardButton(text="📍 Назначение"), KeyboardButton(text="🏢 Компания")],
        [KeyboardButton(text="📞 Телефон"), KeyboardButton(text="💰 Оплата")],
        [KeyboardButton(text="📝 Комментарий"), KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)


def format_cargo_data(data: dict) -> str:
    """Форматирование данных груза для отображения"""
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


def hash_data(data: str) -> str:
    return hashlib.sha256((data + SALT).encode()).hexdigest()


def generate_unique_id(data: dict) -> str:
    raw_data = f"{data['name']}{data['origin']}{data['destination']}{data['company']}{data['phone']}{data['payment']}"
    return hash_data(raw_data)[:10]


async def get_cargo_by_id(shipment_id: str, user_id: int) -> dict:
    """Получение груза по ID"""
    try:
        conn = await asyncpg.connect(**DB_CONFIG)
        cargo = await conn.fetchrow(
            "SELECT * FROM cargo_cargo WHERE shipment_id = $1 AND user_id = $2",
            shipment_id, hash_data(str(user_id)))
        await conn.close()

        if not cargo:
            logger.warning(f"Груз не найден: shipment_id={shipment_id}")
            raise ValueError("Груз не найден или у вас нет прав доступа.")

        return dict(cargo)
    except Exception as e:
        logger.error(f"Ошибка при получении груза: {e}")
        raise


async def get_user_cargos(user_id: int) -> list:
    """Получение всех грузов пользователя"""
    conn = None
    try:
        conn = await asyncpg.connect(**DB_CONFIG)
        query = "SELECT * FROM cargo_cargo WHERE user_id = $1"
        cargos = await conn.fetch(query, hash_data(str(user_id)))
        return [dict(cargo) for cargo in cargos]
    except Exception as e:
        logger.error(f"Ошибка БД: {e}")
        return []
    finally:
        if conn:
            await conn.close()


async def save_to_db(user_id: int):
    """Сохранение груза в БД"""
    conn = await asyncpg.connect(**DB_CONFIG)
    data = user_data[user_id]["data"]

    try:
        await conn.execute(
            """
            INSERT INTO cargo_cargo 
            (shipment_id, name, origin, destination, company, 
             phone, payment, description, user_id)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
            """,
            data["shipment_id"], data["name"], data["origin"],
            data["destination"], data["company"], data["phone"],
            data["payment"], data["description"],
            hash_data(str(user_id)))

        # Отправка сообщения водителям
        driver_message = (
            f"🚛 Новый груз доступен!\n\n"
            f"📦 Груз: {data['name']}\n"
            f"📍 Маршрут: {data['origin']} → {data['destination']}\n"
            f"🏢 Компания: {data['company']}\n"
            f"💰 Оплата: {data['payment']} USD\n"
            f"📞 Контакт: {data['phone']}\n"
            f"📝 Детали: {data['description']}\n"
            f"🔑 Номер: {data['shipment_id']}"
        )

        builder = InlineKeyboardBuilder()
        if data['phone'].startswith('@'):
            builder.button(text="📨 Написать", url=f"https://t.me/{data['phone'][1:]}")
        else:
            clean_phone = re.sub(r'[^\d]', '', data['phone'])
            builder.button(text="📞 Позвонить", url=f"https://t.me/share/phone?phone={clean_phone}")

        try:
            await bot.send_message(
                chat_id=DRIVERS_GROUP_ID,
                text=driver_message,
                reply_markup=builder.as_markup()
            )
        except Exception as e:
            logger.error(f"Ошибка отправки водителям: {e}")

    except Exception as e:
        logger.error(f"Ошибка сохранения: {e}")
        raise
    finally:
        await conn.close()


async def delete_cargo_from_db(shipment_id: str, user_id: int):
    """Удаление груза из БД"""
    conn = await asyncpg.connect(**DB_CONFIG)
    try:
        # Удаление из БД
        result = await conn.execute(
            "DELETE FROM cargo_cargo WHERE shipment_id = $1 AND user_id = $2",
            shipment_id, hash_data(str(user_id)))

        if result == "DELETE 0":
            raise ValueError("Груз не найден")

        # Попытка удалить сообщение из группы
        try:
            chat = await bot.get_chat(DRIVERS_GROUP_ID)
            async for message in bot.get_chat_history(chat.id, limit=100):
                if message.text and f"🔑 {shipment_id}" in message.text:
                    try:
                        await bot.delete_message(chat.id, message.message_id)
                        break
                    except Exception:
                        continue
        except Exception as e:
            logger.error(f"Ошибка при удалении сообщения: {e}")
    except Exception as e:
        logger.error(f"Ошибка удаления: {e}")
        raise
    finally:
        await conn.close()


# Обработчики команд
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Привет! Выберите действие:", reply_markup=main_menu)


@dp.message(lambda message: message.text == "➕ Добавить груз")
async def add_cargo(message: Message):
    user_data[message.chat.id] = {"state": "adding", "data": {}}
    await message.answer("Введите название груза:")


@dp.message(lambda message: message.text == "👀 Мои грузы")
async def show_cargos(message: Message):
    user_id = message.chat.id
    cargos = await get_user_cargos(user_id)

    if not cargos:
        await message.answer("У вас нет сохраненных грузов.")
        return

    await message.answer("📦 Ваши грузы:")

    for cargo in cargos:
        msg = (
            f"🔸 Номер: {cargo['shipment_id']}\n"
            f"📦 Название: {cargo['name']}\n"
            f"🚚 Маршрут: {cargo['origin']} → {cargo['destination']}\n"
            f"💵 Оплата: {cargo['payment']} USD"
        )

        builder = InlineKeyboardBuilder()
        builder.button(text="✏ Редактировать", callback_data=f"edit_{cargo['shipment_id']}")
        builder.button(text="🗑 Удалить", callback_data=f"delete_{cargo['shipment_id']}")

        await message.answer(msg, reply_markup=builder.as_markup())


@dp.callback_query(lambda c: c.data.startswith('delete_'))
async def delete_cargo(callback: CallbackQuery):
    shipment_id = callback.data.replace('delete_', '')
    try:
        await delete_cargo_from_db(shipment_id, callback.from_user.id)
        await callback.answer("Груз удален", show_alert=True)
        await callback.message.delete()
    except Exception as e:
        logger.error(f"Ошибка удаления: {e}")
        await callback.answer("Ошибка удаления", show_alert=True)


@dp.callback_query(lambda c: c.data.startswith('edit_'))
async def edit_cargo(callback: CallbackQuery):
    shipment_id = callback.data.replace('edit_', '')
    user_id = callback.from_user.id

    try:
        cargo = await get_cargo_by_id(shipment_id, user_id)
        user_data[user_id] = {
            "state": "editing",
            "data": cargo,
            "shipment_id": shipment_id
        }
        await callback.message.answer(
            "Выберите поле для редактирования:",
            reply_markup=edit_menu
        )
        await callback.answer()
    except Exception as e:
        logger.error(f"Ошибка редактирования: {e}")
        await callback.answer("Ошибка при редактировании", show_alert=True)


# Обработка редактирования
@dp.message(lambda message: message.text in ["📦 Название", "🚛 Отправление", "📍 Назначение",
                                             "🏢 Компания", "📞 Телефон", "💰 Оплата", "📝 Комментарий"])
async def edit_field(message: Message):
    user_id = message.chat.id
    if user_id not in user_data or user_data[user_id]["state"] != "editing":
        await message.answer("Используйте кнопки меню", reply_markup=main_menu)
        return

    field_map = {
        "📦 Название": "name",
        "🚛 Отправление": "origin",
        "📍 Назначение": "destination",
        "🏢 Компания": "company",
        "📞 Телефон": "phone",
        "💰 Оплата": "payment",
        "📝 Комментарий": "description"
    }

    field = field_map[message.text]
    user_data[user_id]["edit_field"] = field
    await message.answer(f"Введите новое значение для {message.text}:", reply_markup=types.ReplyKeyboardRemove())


# Обработка ввода новых значений
@dp.message()
async def handle_input(message: Message):
    user_id = message.chat.id
    text = message.text

    if user_id not in user_data:
        await message.answer("Используйте кнопки меню", reply_markup=main_menu)
        return

    if user_data[user_id]["state"] == "adding":
        await handle_add_cargo(message)
    elif user_data[user_id]["state"] == "editing" and "edit_field" in user_data[user_id]:
        await handle_edit_field(message)


async def handle_add_cargo(message: Message):
    user_id = message.chat.id
    text = message.text
    data = user_data[user_id]["data"]

    if "name" not in data:
        if 2 <= len(text) <= 100:
            data["name"] = text
            await message.answer("Введите пункт отправления:")
        else:
            await message.answer("Название должно быть 2-100 символов")
    elif "origin" not in data:
        data["origin"] = text
        await message.answer("Введите пункт назначения:")
    elif "destination" not in data:
        data["destination"] = text
        await message.answer("Введите название компании:")
    elif "company" not in data:
        if 2 <= len(text) <= 100:
            data["company"] = text
            keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="📱 Ввести телефон")],
                    [KeyboardButton(text="📲 Использовать Telegram")]
                ],
                resize_keyboard=True
            )
            await message.answer("Выберите способ контакта:", reply_markup=keyboard)
        else:
            await message.answer("Название компании должно быть 2-100 символов")
    elif "phone" not in data:
        if message.text == "📲 Использовать Telegram":
            if message.from_user.username:
                data["phone"] = f"@{message.from_user.username}"
                await message.answer("Введите сумму оплаты (USD):", reply_markup=types.ReplyKeyboardRemove())
            else:
                await message.answer("У вас нет username. Введите телефон:")
        elif re.match(r"^\+?[1-9]\d{1,14}$", text):
            data["phone"] = text
            await message.answer("Введите сумму оплаты (USD):", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("Введите корректный телефон")
    elif "payment" not in data:
        try:
            amount = float(text)
            if amount > 0:
                data["payment"] = amount
                await message.answer("Введите комментарий:")
            else:
                await message.answer("Сумма должна быть > 0")
        except ValueError:
            await message.answer("Введите число")
    elif "description" not in data:
        if len(text) <= 500:
            data["description"] = text
            data["shipment_id"] = generate_unique_id(data)
            try:
                await save_to_db(user_id)
                await message.answer(
                    f"✅ Груз сохранен!\n{format_cargo_data(data)}",
                    reply_markup=main_menu
                )
                del user_data[user_id]
            except Exception:
                await message.answer("Ошибка сохранения", reply_markup=main_menu)
        else:
            await message.answer("Комментарий слишком длинный (макс 500 симв)")


async def handle_edit_field(message: Message):
    user_id = message.chat.id
    text = message.text
    field = user_data[user_id]["edit_field"]
    shipment_id = user_data[user_id]["shipment_id"]

    # Валидация ввода
    valid = True
    if field == "name" and not (2 <= len(text) <= 100):
        await message.answer("Название должно быть 2-100 символов")
        valid = False
    elif field == "company" and not (2 <= len(text) <= 100):
        await message.answer("Название компании должно быть 2-100 символов")
        valid = False
    elif field == "phone" and not re.match(r"^\+?[1-9]\d{1,14}$", text) and not text.startswith("@"):
        await message.answer("Введите корректный телефон или @username")
        valid = False
    elif field == "payment":
        try:
            amount = float(text)
            if amount <= 0:
                await message.answer("Сумма должна быть > 0")
                valid = False
            else:
                text = amount
        except ValueError:
            await message.answer("Введите число")
            valid = False
    elif field == "description" and len(text) > 500:
        await message.answer("Комментарий слишком длинный (макс 500 симв)")
        valid = False

    if not valid:
        return

    # Обновление в БД
    conn = None
    try:
        conn = await asyncpg.connect(**DB_CONFIG)
        await conn.execute(
            f"UPDATE cargo_cargo SET {field} = $1 WHERE shipment_id = $2 AND user_id = $3",
            text, shipment_id, hash_data(str(user_id)))

        # Обновляем данные в user_data
        user_data[user_id]["data"][field] = text

        await message.answer(
            f"✅ Поле успешно обновлено!\n{format_cargo_data(user_data[user_id]['data'])}",
            reply_markup=main_menu
        )
        del user_data[user_id]
    except Exception as e:
        logger.error(f"Ошибка обновления: {e}")
        await message.answer("Ошибка при обновлении", reply_markup=main_menu)
    finally:
        if conn:
            await conn.close()


async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Ошибка: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())