
for i in range(1,5):
    print(i,
          end=" | ")
    for j in range(1,11):
        print(j,
              end=" ")
    print()

print()
# # # 1. Створіть список з англійських назв днів тижня.
# # # Змініть список таким чином, щоб в ньому знаходились кортежі (i, j, t,v), де i- індекс дня тижня, починаючи з 10, а j – назва дня тижня, t – кількість символів в дні тижня, v – булеве значення True/False, в залежності чи t парне, чи ні.
# # Тобто [‘Monday’, ...]  -> [(10, ‘Monday’,6, True), ...]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i,day in enumerate(days_of_week):
    days_of_week[i] = (10 + i,
                       day,
                       len(day),
                       len(day) % 2 == 0)

for day in days_of_week:
    print(f'Index: {day[0]}, Name of weekday: {day[1]}, Len of the weekday: {day[2]}, Even value: {day[3]}')

print()

# # # 2. З допомогою циклу for та ф-ії range потрібно отримати кортеж чисел, кратних 13, в діапазоні від 3 до 231.

tupple_1 = ()
for i in range(3,231):
    if i % 13 == 0:
        tupple_1 = tupple_1 + (i,)

print(tupple_1)

# 3. Вирішити задачу 2 з допомогою циклу while

tupple_2 = ()
counter = 3
while counter < 231:
    if counter % 13 == 0:
        tupple_2 = tupple_2 + (counter,)
    counter += 1

print(tupple_2)
print("\n")
# # # 4.Вивести табличку множення, від 1 до 10.
# # # Зверху і зліва мають виводитись множники, відділені від результату (дивись картинку). Числа повинні бути відформатовні по лівому краю (як зробити ? Виконати research google)

list_2 = [""]
for i in range(1, 11):
    list_2.append(i)


for i in list_2:
    if i == "":
        print("      ", end="")
    else:
        print(f"{i:3}", end=" ")

print('\n\t  ' + '-' * 39)


for i in range(1, 11):
    print(f"{i:3}", end=" | ")
    for value in list_2[1:]:
        print(f"{i * value:3}", end=" ")
    print()

print("\n")
# # 5. Потрібно згенерувати всі варіанти коду. Відомо, що код складається з 3 розрядів: 2 перші містять цифри від 0 до 9,  останній – символи англійського алфавіту в верхньому регістрі, тобто від A до Z, наприклад:  09D, 65T
# # а) Результат потрібно зберегти в списку, і вивести довжину списку
# # б) Результат потрібно зберегти в словнику, де ключ буде визначати номер варіанту коду, починаючи з 1, а значення – власне сам код.

import random
import string

random_numbers_1 = []

alphabet = list(string.ascii_uppercase)
new =[]

while len(random_numbers_1) < 9:
    random_numbers_1.append(random.randint(1,9))
counter = 0
while counter < 26:
    print(
        f'{random_numbers_1[random.randint(0, 8)]}{random_numbers_1[random.randint(0, 8)]}{alphabet[random.randint(0, 25)]}', end=" | ")
    counter +=1


print()
print(f'List content: {random_numbers_1}, Length of the list is: {len(random_numbers_1)}')
print(f'List content: {alphabet}, Length of the list is: {len(alphabet)}')



client = {'name':'Andrii', 'sex':'m'}
print(client['name'])

for i,j in client.items():
    print(i,j)

# Dictionary Generator (key:value)
my_list = {i:i**2 for i in range(10) if i%2 == 0}
print(my_list)