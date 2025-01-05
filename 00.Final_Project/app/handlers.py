from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


# Ответ на команду /start отправка сообщения пользователю
# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer('Привет')

# Ответ на команду /start ответ на сообщение пользователя
@dp.message(CommandStart())
async def cmd_start(message: Message):
    # Отправляем сообщение пользователю с его ID и именем
    await message.reply(f'Привет. \nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')


# Ответ на команду /help
@dp.message(Command('help'))
async def get_help(message: Message):
    # Отправляем пользователю текст с описанием команды
    await message.answer('Это команда /help')


# Ответ на сообщение с текстом "Как дела?"
@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    # Отвечаем пользователю "OK!"
    await message.answer('OK!')


# Отправка изображения по команде /get_photo (ссылка на изображение)
@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    # Отправляем изображение по URL и добавляем подпись
    await message.answer_photo(
        photo='https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/512px-Telegram_2019_Logo.svg.png',
        caption='Это лого ТГ'
    )


# @dp.message(Command('get_photo'))  # Отправляем картинку зная ее id
# async def get_photo(message: Message):
#     await message.answer_photo(
#         photo='AgACAgIAAxkBAAMkZ3l27KpjR8RuJoGP6NldK3cSRBoAAibqMRuQJMlLRxLZi_SOTZYBAAMCAAN5AAM2BA',
#         caption='Это лого ТГ')

# Обработка сообщений с фотографиями
@dp.message(F.photo)
async def get_photo(message: Message):
    # Получаем ID загруженной фотографии и отправляем его обратно пользователю
    await message.answer(f'ID фото {message.photo[-1].file_id}')
