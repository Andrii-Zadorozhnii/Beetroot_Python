#a = 'kolobok'
from numpy.random import randn

#for i in range(len(a)):
#    print(f'Index {i}: {a[i].upper()}')


#Задачі до уроку 4:

#1. Прорахуйте результат, потім перевірте в коді:
#(True and not True and True)
print(True and not True and True) # False
#(True and True or True)
print(True and True or True)    #True
# (False or True or not False)
print(False or True or not False)   #True
#(False and True and False)
print(False and True and False) #False

#2. Який оператор (and, or) неявно використовується при множинному порівнянні ?
#Розберіть на прикладах, перевірте в коді:
#(2<3<4<5)
print(2<3<4<5) #True and
# (4>3<6<9)
print(4<3<6<9) #True and

#3. Створіть код (з використанням if) який буде виводити назву дня тижня в залежності від значення змінної day_name, яка може приймати значення 1..7.

day_time = int(input("Weekday number : "))

if day_time == 1:
    print("Monday")
elif day_time == 2:
    print("Tuesday")
elif day_time == 3:
    print("Wednesday")
elif day_time == 4:
    print("Thursday")
elif day_time == 5:
    print('Friday')
elif day_time == 6:
    print("Saturday")
elif day_time == 7:
    print("Sunday")
else:
    print('Incorrect input =(')

#4. Ускладніть код з п.3, додавши змінну d_n, яка може приймати значення ‘day’, ‘night’. Виведіть день тижня та пору дня.

day_time = int(input("Weekday number : "))
d_n = input("Day or night? format(d/n):")

if day_time == 1:
    print("Monday")

elif day_time == 2:
    print("Tuesday")
    if d_n == "d":
        print('day time')
    elif d_n == "n":
        print('nigh time')
elif day_time == 3:
    print("Wednesday")
    if d_n == "d":
        print('day time')
    elif d_n == "n":
        print('nigh time')
elif day_time == 4:
    print("Thursday")
    if d_n == "d":
        print('day time')
    elif d_n == "n":
        print('nigh time')
elif day_time == 5:
    print('Friday')
    if d_n == "d":
        print('day time')
    elif d_n == "n":
        print('nigh time')
elif day_time == 6:
    print("Saturday")
    if d_n == "d":
        print('day time')
    elif d_n == "n":
        print('nigh time')
elif day_time == 7:
    print("Sunday")
    if d_n == "d":
        print('day time')
    elif d_n == "n":
        print('nigh time')
else:
    print('Incorrect input =(')

#5. В циклі while задайте умову для проходження змінної my_number від 1 до 25 (при кожному проході виводьте на прінт значення my_number), але зупиніть виконання коли my_number буде ділитись без остачі на 3 і на 7.
my_number = 0

while my_number <= 25:
    my_number = my_number + 1
    print(my_number)
    if my_number % 3 == 0 and my_number % 7 == 0:
        break




#6. Змініть код попередньої задачі таким чином, щоб значення my_number не виводилось на прінт, коли my_number буде ділитись без остачі на 3 і на 7.

my_number = 0

while my_number <= 25:
    my_number = my_number + 1

    if my_number % 3 == 0 and my_number % 7 == 0:
        break
    print(my_number)

#7. Виведіть з допомогою циклу for всі літери з ‘qwerty’

latter = "qwerty"

for i in latter:
    print(i)

#8. Ускладнення попередньої задачі. Виведіть індекс літери та саму літеру 2-ма способами (range, len; enumerate).

latter = "qwerty"

for i in range(len(latter)):
    print(f'Index {i}: {latter[i].upper()}')

for i, char in enumerate(latter):
    print(f'Index {i}: {char}')

#9. Перепишіть код задач 5 та 6, використовуючи цикл for.

number_1 = 25

for i in range(number_1):
    print(i)
    if i % 3 == 0 and i % 7 == 0:
        break

