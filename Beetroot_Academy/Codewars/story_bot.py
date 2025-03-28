from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Глобальные переменные
user_state = {}  # Хранит состояние пользователя (какая глава сюжета активна)


# Начало диалога с ботом
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_state[user_id] = "start"  # Начальная глава сюжета
    await update.message.reply_text(
        "Ты просыпаешься в туманном лесу, не помня, как сюда попала. Вокруг слышны странные звуки.\n"
        "Ты ощущаешь тревогу. Что делать?\n\n"
        "1. Пойти в сторону светлого леса\n"
        "2. Остаться на месте и прислушаться",
        reply_markup=ReplyKeyboardMarkup([["1. Пойти в сторону светлого леса", "2. Остаться на месте"]],
                                         one_time_keyboard=True),
    )


# Обработка выбора пользователя
async def handle_choice(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    choice = update.message.text

    if user_id not in user_state:
        return

    # Логика для каждой главы сюжета
    if user_state[user_id] == "start":
        if choice == "1. Пойти в сторону светлого леса":
            await update.message.reply_text(
                "Ты идешь в сторону светлого леса. Вдруг слышишь странный шум. Что делать?\n\n"
                "1. Прятаться за дерево\n"
                "2. Идти дальше, не обращая внимания",
                reply_markup=ReplyKeyboardMarkup([["1. Прятаться за дерево", "2. Идти дальше"]],
                                                 one_time_keyboard=True),
            )
            user_state[user_id] = "chapter_1"
        elif choice == "2. Остаться на месте":
            await update.message.reply_text(
                "Ты остаешься на месте и прислушиваешься. Вдруг видишь тень, двигающуюся среди деревьев. Что делать?\n\n"
                "1. Подойти к тени\n"
                "2. Закрыть глаза и надеяться, что тень уйдет",
                reply_markup=ReplyKeyboardMarkup([["1. Подойти к тени", "2. Закрыть глаза"]], one_time_keyboard=True),
            )
            user_state[user_id] = "chapter_2"

    elif user_state[user_id] == "chapter_1":
        if choice == "1. Прятаться за дерево":
            await update.message.reply_text(
                "Ты прячешься за дерево, но звуки становятся все громче. Появляется огромное существо, похожее на дракона.\n\n"
                "1. Попробовать убежать\n"
                "2. Сражаться с существом",
                reply_markup=ReplyKeyboardMarkup([["1. Попробовать убежать", "2. Сражаться"]], one_time_keyboard=True),
            )
            user_state[user_id] = "chapter_3"
        elif choice == "2. Идти дальше":
            await update.message.reply_text(
                "Ты продолжаешь идти, но существо замечает тебя и бросается в твою сторону.\n\n"
                "Ты не успеваешь укрыться... Ты теряешь сознание. Конец.",
            )
            user_state[user_id] = "game_over"

    elif user_state[user_id] == "chapter_2":
        if choice == "1. Подойти к тени":
            await update.message.reply_text(
                "Ты подходишь ближе, и вдруг тень становится человеком. Это девушка. Она говорит: 'Помоги мне выбраться отсюда!'\n\n"
                "1. Попросить её рассказать больше\n"
                "2. Попросить её идти за тобой",
                reply_markup=ReplyKeyboardMarkup([["1. Попросить рассказать", "2. Попросить идти за тобой"]],
                                                 one_time_keyboard=True),
            )
            user_state[user_id] = "chapter_4"
        elif choice == "2. Закрыть глаза":
            await update.message.reply_text(
                "Ты закрываешь глаза, надеясь, что тень уйдет, но чувствуешь, как она приближается. Она шепчет: 'Ты не сможешь уйти отсюда, пока не примешь решение.'\n\n"
                "Ты открываешь глаза и видишь ее перед собой. Конец.",
            )
            user_state[user_id] = "game_over"

    elif user_state[user_id] == "chapter_4":
        if choice == "1. Попросить рассказать":
            await update.message.reply_text(
                "Девушка рассказывает, что она потерялась в этом лесу и не может выбраться. Она предлагает свою помощь в обмен на твою.\n\n"
                "1. Попросить её показывать путь\n"
                "2. Сказать, что ты сам ищешь выход",
                reply_markup=ReplyKeyboardMarkup(
                    [["1. Попросить показывать путь", "2. Сказать, что ты сам ищешь выход"]], one_time_keyboard=True),
            )
            user_state[user_id] = "chapter_5"
        elif choice == "2. Попросить идти за тобой":
            await update.message.reply_text(
                "Ты говоришь ей идти за тобой, но она исчезает в тумане. Ты остаешься один.\n\n"
                "Ты чувствуешь, как лес окружает тебя, и всё становится темнее. Конец.",
            )
            user_state[user_id] = "game_over"


# Главная функция для запуска бота
def main() -> None:
    application = Application.builder().token("7815057084:AAF4VzGv3cHYcJqNIh93CPe7NEj3tx40Ql0").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_choice))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()