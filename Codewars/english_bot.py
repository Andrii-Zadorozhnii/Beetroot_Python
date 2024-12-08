from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Словарь заданий
tasks = {
    "Beginner": {
        "words": [
            {"word": "cat", "translation": "кот"},
            {"word": "run", "translation": "бегать"},
            {"word": "book", "translation": "книга"},
        ],
        "grammar": [
            {"sentence": "I ____ a book every day.", "options": ["read", "reads"], "answer": "read"},
            {"sentence": "She ____ to school.", "options": ["go", "goes"], "answer": "goes"},
        ],
    },
    "Intermediate": {
        "words": [
            {"word": "diligent", "translation": "усердный"},
            {"word": "achieve", "translation": "достигать"},
        ],
        "grammar": [
            {"sentence": "If I ____ time, I will help you.", "options": ["have", "had"], "answer": "have"},
            {"sentence": "They ____ been working here for years.", "options": ["has", "have"], "answer": "have"},
        ],
    },
    "Advanced": {
        "words": [
            {"word": "serendipity", "translation": "интуитивная удача"},
            {"word": "contemplate", "translation": "размышлять"},
        ],
        "grammar": [
            {"sentence": "Had I known, I ____ have acted differently.", "options": ["would", "will"],
             "answer": "would"},
            {"sentence": "The book, ____ I bought yesterday, is fantastic.", "options": ["which", "that"],
             "answer": "which"},
        ],
    },
}


# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup([["Beginner", "Intermediate", "Advanced"]], one_time_keyboard=True)
    await update.message.reply_text(
        "Привет! Выберите уровень сложности для изучения английского:",
        reply_markup=reply_markup,
    )


# Установка уровня
async def set_level(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    level = update.message.text
    if level not in tasks:
        await update.message.reply_text(
            "Пожалуйста, выберите один из доступных уровней: Beginner, Intermediate, Advanced.")
        return
    context.user_data["level"] = level
    context.user_data["mode"] = "words"
    await update.message.reply_text(f"Вы выбрали уровень {level}. Напишите /train, чтобы начать тренировку.")


# Тренировка
async def train(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    level = context.user_data.get("level")
    if not level:
        await update.message.reply_text("Сначала выберите уровень сложности, используя команду /start.")
        return

    mode = context.user_data.get("mode", "words")
    if mode == "words":
        task = random.choice(tasks[level]["words"])
        context.user_data["current_task"] = task
        await update.message.reply_text(f"Как переводится слово: {task['word']}?")
        context.user_data["mode"] = "grammar"
    elif mode == "grammar":
        task = random.choice(tasks[level]["grammar"])
        context.user_data["current_task"] = task
        options = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(task["options"])])
        await update.message.reply_text(f"{task['sentence']}\n\nВыберите правильный вариант:\n{options}")
        context.user_data["mode"] = "words"


# Проверка ответа
async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_answer = update.message.text.strip().lower()
    task = context.user_data.get("current_task")
    if not task:
        await update.message.reply_text("Сначала начните тренировку с помощью команды /train.")
        return

    # Проверяем слова или грамматику
    if "translation" in task:
        if user_answer == task["translation"]:
            await update.message.reply_text("Правильно! 🎉")
        else:
            await update.message.reply_text(f"Неправильно. Правильный перевод: {task['translation']}")
    elif "answer" in task:
        correct_option = task["answer"]
        if user_answer == correct_option or user_answer.isdigit() and task["options"][
            int(user_answer) - 1] == correct_option:
            await update.message.reply_text("Правильно! 🎉")
        else:
            await update.message.reply_text(f"Неправильно. Правильный ответ: {correct_option}")

    context.user_data["current_task"] = None
    await train(update, context)


# Основной код
def main() -> None:
    application = Application.builder().token("7815057084:AAF4VzGv3cHYcJqNIh93CPe7NEj3tx40Ql0").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("train", train))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

    application.run_polling()


if __name__ == "__main__":
    main()