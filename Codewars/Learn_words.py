from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Расширенный словарь с задачами
tasks = {
    "Beginner": {
        "words": [
                     {"word": "cat", "translation": "кот"},
                     {"word": "run", "translation": "бегать"},
                     {"word": "book", "translation": "книга"},
                     {"word": "dog", "translation": "собака"},
                     {"word": "happy", "translation": "счастливый"},
                     {"word": "school", "translation": "школа"},
                     # Добавляем больше слов...
                 ] + [{"word": f"word_{i}", "translation": f"перевод_{i}"} for i in range(7, 101)],
        "grammar": [
                       {"sentence": "I ____ a book every day.", "options": ["read", "reads"], "answer": "read"},
                       {"sentence": "She ____ to school.", "options": ["go", "goes"], "answer": "goes"},
                       {"sentence": "We ____ at home yesterday.", "options": ["were", "was"], "answer": "were"},
                       {"sentence": "He ____ a teacher.", "options": ["is", "are"], "answer": "is"},
                       # Добавляем больше грамматических задач...
                   ] + [{"sentence": f"Task {i}: He ____ apples.", "options": ["likes", "like"], "answer": "likes"} for
                        i in range(5, 101)],
    },
    "Intermediate": {
        "words": [
                     {"word": "diligent", "translation": "усердный"},
                     {"word": "achieve", "translation": "достигать"},
                     {"word": "fortunate", "translation": "удачливый"},
                     {"word": "delight", "translation": "радость"},
                     {"word": "journey", "translation": "путешествие"},
                     {"word": "reflect", "translation": "размышлять"},
                     # Добавляем больше слов...
                 ] + [{"word": f"word_{i}", "translation": f"перевод_{i}"} for i in range(7, 101)],
        "grammar": [
                       {"sentence": "If I ____ time, I will help you.", "options": ["have", "had"], "answer": "have"},
                       {"sentence": "They ____ been working here for years.", "options": ["has", "have"],
                        "answer": "have"},
                       {"sentence": "The train ____ already left.", "options": ["has", "have"], "answer": "has"},
                       # Добавляем больше грамматических задач...
                   ] + [{"sentence": f"Task {i}: We ____ to the beach last week.", "options": ["went", "go"],
                         "answer": "went"} for i in range(4, 101)],
    },
    "Advanced": {
        "words": [
                     {"word": "serendipity", "translation": "интуитивная удача"},
                     {"word": "contemplate", "translation": "размышлять"},
                     {"word": "oblivion", "translation": "забвение"},
                     {"word": "ephemeral", "translation": "мимолетный"},
                     {"word": "ubiquitous", "translation": "повсеместный"},
                     {"word": "meticulous", "translation": "дотошный"},
                     # Добавляем больше слов...
                 ] + [{"word": f"word_{i}", "translation": f"перевод_{i}"} for i in range(7, 101)],
        "grammar": [
                       {"sentence": "Had I known, I ____ have acted differently.", "options": ["would", "will"],
                        "answer": "would"},
                       {"sentence": "The book, ____ I bought yesterday, is fantastic.", "options": ["which", "that"],
                        "answer": "which"},
                       {"sentence": "He acts as if he ____ the boss.", "options": ["is", "were"], "answer": "were"},
                       # Добавляем больше грамматических задач...
                   ] + [{"sentence": f"Task {i}: No sooner ____ he arrived than the meeting began.",
                         "options": ["had", "has"], "answer": "had"} for i in range(4, 101)],
    },
}


# Команда /start
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
    await next_task(update, context)


# Следующее задание
async def next_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
        await update.message.reply_text("Сначала начните тренировку с помощью выбора уровня.")
        return

    if "translation" in task:
        if user_answer == task["translation"]:
            await update.message.reply_text("Правильно! 🎉")
        else:
            await update.message.reply_text(f"Неправильно. Правильный перевод: {task['translation']}")
    elif "answer" in task:
        correct_option = task["answer"]
        if user_answer == correct_option or (
                user_answer.isdigit() and task["options"][int(user_answer) - 1] == correct_option):
            await update.message.reply_text("Правильно! 🎉")
        else:
            await update.message.reply_text(f"Неправильно. Правильный ответ: {correct_option}")

    await next_task(update, context)


# Основной код
def main() -> None:
    application = Application.builder().token("7815057084:AAF4VzGv3cHYcJqNIh93CPe7NEj3tx40Ql0").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex("^(Beginner|Intermediate|Advanced)$"), set_level))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))

    application.run_polling()


if __name__ == "__main__":
    main()