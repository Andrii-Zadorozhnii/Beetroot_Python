lang = "python"
print(lang[0], lang[2], lang[len(lang) - 1]) # Виведіть в одному рядку символи ‘p’, ‘t’ ‘n’ з цього слова, використовуючи доступ через індекси. Для виведення останнього символу (‘n’ ) використайте функцію len().

print(lang.capitalize()) # перший символ – велика буква
print(lang.upper()) # всі символі – великі букви
print(type(lang)) # Визначте тип змінної lang.

print(7//2) # цілий залишок від ділення 7 на 2
print(7%2) # остача від ділення 7 на 2
print(3**4) # 3 в степені 4
print(str(7//2),str(7%2), str(3**4))
a = 1.51
print(int(a)) # переведення числа в int
print(round(a)) # округлення через round
pi = 3.141592
print(round(pi,3)) # округліть число пі (3,141592) до 3 знаків після коми.

print ( (20+3)*5,
6**2-50/5,
6**(5-2)/5,
4/2**3,
15//4%2 ) # 8 дуже просте
print()
#Виконайте перетворення типів (int, str, float), всі можливі варіанти для наступних даних. В кожному випадку постарайтесь зрозуміти результат.
# print(int(9))
# print(str(9))
# print(float(9))
# print(int(12.0))
# print(str(12.0))
# print(float(12.0))
# print(int(12.3))
# print(str(12.3))
# print(float(12.3))
# print(int('12'))
# print(str('12'))
# print(float('12'))
# print(int('23.7'))
# print(str('23.7'))
# print(float('23.7'))
# print(int(‘qwerty’))
# print(str(‘qwerty’))
# print(float(‘qwerty’)®)

#Створіть змінну типу str з нульовою довжиною.

zero_lengh = ""
print('Length is: ' + str(len(zero_lengh)))
#11. Створіть будь-який текст, застосувавши для нього:
# - одинарні лапки
print(
    'hello world!'
)
# - подвійні
print(
    "Hello world!"
)
# - потрійні (розмістіть текст в кількох рядках)
print(
    """
Hello
World
!
    """
)
#12. результатом print() повинні бути:
# - student’s book
# - “Kyiv”
print("student’s book")
print("Kyiv")

#13. Продемонструйте в коді 2 варіанти використання зворотнього слешу
print("This is a \"quote\".")
print("This is a long string \
that is split into two lines.")
#14. Яка довжина рядка ‘qwe rty’ ? Спрогнозуйте, потім перевірте в коді.
string = 'qwe rty'
print(len(string))
#15. Є змінна a=’qwerty’. Потрібно отримати наступний результат:
#qwertyqwertyqwerty
# Реалізуйте мінімум 2-ма методами.
a = 'qwerty'
print(a * 3)
print(a + a + a)
#16. Є змінна beta=’qwerty’.
#Реалізуйте настуні операції, використовуючи методи для роботи з рядками:


beta = 'qwerty'

# Визначте довжину
print(len(beta))  # 6

# Підрахуйте кількість символів 'y'
print(beta.count('y'))  # 1

# Отримайте слово в верхньому та нижньому регістрах
print(beta.upper())  # 'QWERTY'
print(beta.lower())  # 'qwerty'

# Зробіть так, щоб значення змінної beta було 'QWERTY'
beta = beta.upper()
print(beta)  # 'QWERTY'

# Замініть 'T' на 'y'
beta = beta.replace('T', 'y')
print(beta)  # 'QWERYy'

# Перевірте, чи змінна beta містить лише символи, або лише цифри
print(beta.isalpha())  # True (лише символи)
print(beta.isdigit())  # False (не цифри)

# Перевірте, чи 'W' входить в змінну beta
print('W' in beta)  # True
#17. знайдіть символи ‘q’ та ‘Q’ у змінній beta=’QWERTY’ при допомозі методів .index() та .find().
beta = 'QWERTY'

# Знайти позицію 'q' (не знайде, тому викликає помилку)
# print(beta.index('q'))  # Помилка

# Знайти позицію 'Q'
print(beta.index('Q'))
print(beta.find('Q'))

#18. знайдіть в ‘qwertyqwerty’ символ ‘t’ при допомозі методів .find() та .rfind(). Зрозуміло, чому результати (індекси) різні ?
string = 'qwertyqwerty'

# find повертає перше входження
print(string.find('t'))

# rfind повертає останнє входження
print(string.rfind('t'))

#19. Отримайте з ‘qwerty’ символи ‘y’, ‘e’, ‘q’ використовуючи зворотню індексацію (індекси з від’ємним значенням).
string = 'qwerty'
print(string[-1])
print(string[-2])
print(string[-6])
#20. Отримайте з ‘qwerty’ при допомозі зрізу ‘wer’:

string = 'qwerty'

# використовуючи додатні індекси
print(string[1:4])

# використовуючи додатній та від’ємний індекс
print(string[1:-2])

# використовуючи від’ємні індекси
print(string[-5:-2])
#21. Отримайте з ‘qwerty’ при допомозі зрізу з кроком ‘wt’
string = 'qwerty'
print(string[::2])

#22. З допомогою шорткатів зрізів з ‘qwerty’ отримайте:
# ‘qwert’, ‘erty’, ‘qwerty’, ‘qet’
string = 'qwerty'

print(string[:5])  # 'qwert'
print(string[1:])  # 'werty'
print(string[:])   # 'qwerty'
print(string[::2])  # 'qet'

#24. Маємо змінні a = ‘Zen’, b = ‘Python’, c=‘Tim’.
#З допомогою різних типів форматування (f-стрічка, format, format з індексами, %) виведіть результат:
#The Zen of Python, by Tim Peters
a = 'Zen'
b = 'Python'
c = 'Tim'

# f-стрічка
print(f"The {a} of {b}, by {c} Peters")

# .format
print("The {} of {}, by {} Peters".format(a, b, c))

# .format з індексами
print("The {0} of {1}, by {2} Peters".format(a, b, c))

# % форматування
print("The %s of %s, by %s Peters" % (a, b, c))

#25. Є змінні PI = ‘Pi is equal to’ та pi = 3.1415.
# Виведіть ‘Pi is equal to 3.14’, використавши форматування з заокругленням до 2 знаків після коми.
PI = 'Pi is equal to'
pi = 3.1415
print(f"{PI} {pi:.2f}")  # "Pi is equal to 3.14"

#26. Переписати вирази для операцій над змінною з допомогою шорткатів:
#n=n+1
#n=n-1
#n=n/1
#n=n*1
#n=n**5

n += 1  # n = n + 1
n -= 1  # n = n - 1
n /= 1  # n = n / 1
n *= 1  # n = n * 1
n **= 5 # n = n ** 5











