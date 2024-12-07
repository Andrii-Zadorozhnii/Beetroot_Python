from prettytable import PrettyTable

# Данные для таблицы
zen_data = [
    ("Красота лучше уродства.", "Beautiful is better than ugly."),
    ("Явное лучше неявного.", "Explicit is better than implicit."),
    ("Простое лучше сложного.", "Simple is better than complex."),
    ("Сложное лучше запутанного.", "Complex is better than complicated."),
    ("Плоское лучше вложенного.", "Flat is better than nested."),
    ("Разреженное лучше плотного.", "Sparse is better than dense."),
    ("Читаемость имеет значение.", "Readability counts."),
    ("Особые случаи не настолько особые, чтобы нарушать правила.",
     "Special cases aren't special enough to break the rules."),
    ("Хотя практичность важнее безупречности.", "Although practicality beats purity."),
    ("Ошибки никогда не должны замалчиваться.", "Errors should never pass silently."),
    ("Если они не замалчиваются явно.", "Unless explicitly silenced."),
    ("Встретив двусмысленность, отбрось искушение угадать.",
     "In the face of ambiguity, refuse the temptation to guess."),
    ("Должен быть один — и, желательно, только один — очевидный способ сделать это.",
     "There should be one-- and preferably only one --obvious way to do it."),
    ("Хотя он поначалу может быть и не очевиден, если вы не голландец.",
     "Although that way may not be obvious at first unless you're Dutch."),
    ("Сейчас лучше, чем никогда.", "Now is better than never."),
    ("Хотя никогда зачастую лучше, чем прямо сейчас.",
     "Although never is often better than *right* now."),
    ("Если реализацию сложно объяснить — идея плоха.",
     "If the implementation is hard to explain, it's a bad idea."),
    ("Если реализацию легко объяснить — идея, возможно, хороша.",
     "If the implementation is easy to explain, it may be a good idea."),
    ("Пространства имен — отличная штука! Давайте делать их больше!",
     "Namespaces are one honking great idea -- let's do more of those!")
]

# Создание таблицы
table = PrettyTable()
table.field_names = ["№", "На русском", "In English"]

for idx, (ru, en) in enumerate(zen_data, start=1):
    table.add_row([idx, ru, en])

# Вывод таблицы
print(table)