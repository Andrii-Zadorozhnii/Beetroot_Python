from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


# python -m venv .venv
# и заходим в папку с проектом .venv
# .venv/Script/activate

# Ответ на команду /start отправка сообщения пользователю
# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer('Привет')


# Ответ на команду /start ответ на сообщение пользователя
@router.message(CommandStart())
async def cmd_start(message: Message):
    # Отправляем сообщение пользователю с его ID и именем
    await message.reply(f'Привет {message.from_user.first_name}',
                        reply_markup=kb.main)
    # \nТвой ID: {message.from_user.id}\nИмя


# Ответ на команду /help
@router.message(Command('help'))
async def get_help(message: Message):
    # Отправляем пользователю текст с описанием команды
    await message.answer('Это команда /help')


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара',
                         reply_markup=kb.catalog)


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    # await callback.answer('Вы выбрали категорию', show_alert=True)
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категории футболок')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data['name']}\nВаш возраст: {data['age']}\nВаш номер телефона: {data['number']}')
    await state.clear()


# Ответ на сообщение с текстом "Как дела?"
@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    # Отвечаем пользователю "OK!"
    await message.answer('OK!')


# Отправка изображения по команде /get_photo (ссылка на изображение)
@router.message(Command('get_photo'))
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
@router.message(F.photo)
async def get_photo(message: Message):
    # Получаем ID загруженной фотографии и отправляем его обратно пользователю
    await message.answer(f'ID фото {message.photo[-1].file_id}')
