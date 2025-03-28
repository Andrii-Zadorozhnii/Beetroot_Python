#
# Задачі:
# З допомогою генератора списку згенерувати 2 масиви випадкових цілих чисел на 100 (значення в межах від 1 до 100) та 10 000 (значення в межах від 1 в межах до 10 000) елементів відповідно.
# Реалізувати лінійний та бінарний пошук.
# Знайти числа 50 та 5 000 для першого та другого списку відповідно.
# Виконати пошук по 3 рази, знайти середнє значення часу на пошук.
# Зробити висновок про складність алгоритмів лінійного та бінарного пошуку в нотації Big O.
# 2. Створіть клас, який ініціалізується будь-яким значенням (value) не мутабельного типу даних.
# Створіть кілька екземплярів цього класу та порівняйте їх між собою.
# Для порівняння реалізуйте наступний алгоритм:
# спочатку порівнюються хеші від value. Якщо вони однакові, то можливо значення рівні і далі порівнюються самі значення. Якщо ж вони не однакові, то екземпляри вважаються не рівними.
# Порівняйте швидкодію такого підходу зі звичайним порівнянням , наприклад створивши 2 списки по 10 елементів з рядків об’єктів, в яких співпадають лише 1-2 елементи.

import random
import time

list_1 = [random.randint(1, 100) for i in range(100)]
list_2 = [random.randint(1, 10000) for j in range(10000)]


class Search:
    def __init__(self, list_1, list_2, search_item):
        self.list_1 = sorted(list_1)
        self.list_2 = sorted(list_2)
        self.search_item = search_item

    def linear_search(self, search_list, search_item):
        step = 0
        for i in range(len(search_list)):
            if search_list[i] == search_item:
                return f"Found item {search_item} at index {i}, steps: {step}"
            else:
                step += 1
        return f"Item {search_item} not found, steps: {step}"

    def binary_search(self, search_list, search_item):
        step = 0
        mid = len(search_list) // 2

        if search_list[mid] == search_item:
            step = 1
            return f"Found item {search_item} at index {mid}, steps: {step}"
        elif search_item not in search_list:
            return f"Item {search_item} not found, steps: {step}"
        elif search_list[mid] < search_item:
            new_list = search_list[mid:]
            step += 1
            return self.binary_search(new_list, search_item)
        elif search_list[mid] > search_item:
            new_list = search_list[:mid]
            step += 1
            return self.binary_search(new_list, search_item)

    def search_calculation(self, func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'{(end - start)} seconds to find the item')
        print(result)

    def linear(self):
        self.search_calculation(self.linear_search, self.list_1, self.search_item)

    def binary(self):
        self.search_calculation(self.binary_search, self.list_1, self.search_item)


search_1 = Search(list_1, list_2, 50)
search_2 = Search(list_2, list_1, 5000)
print(
    '\n Linear Search\n'
)
search_1.linear()
search_1.linear()
search_1.linear()
print(
    '\n Linear Search\n'
)
search_2.linear()
search_2.linear()
search_2.linear()
print(
    '\n Binary Search\n'
)
search_1.binary()
search_1.binary()
search_1.binary()
print(
    '\n Binary Search\n'
)
search_2.binary()
search_2.binary()
search_2.binary()
