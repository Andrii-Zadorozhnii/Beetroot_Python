# Задание 1
#
# Создайте собственную реализацию встроенной функции enumerate с именем «with_index»,
# которая принимает два параметра: «iterable» и «start», значение по умолчанию — 0.
# Советы: см. документацию по функции enumerate.

print(
    '''
Task 1
    '''
)


def with_index(iterable, start=0):
    for item in iterable:
        yield (start, item)
        start += 1


fruits = ["apple", "banana", "cherry"]

for index, value in with_index(fruits):
    print(
        f"Index: {index}, Value: {value.title()}"
    )

# Задание 2
#
# Создайте собственную реализацию встроенной функции range с именем in_range(),
# которая принимает три параметра: 'start', 'end' и необязательный шаг.
# Советы: см. документацию по функции 'range'

print(
    '''
Task 2
    '''
)


def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("Step cannot be zero.")  # Проверка на недопустимый шаг

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step


for number in in_range(0, 10, 2):
    print(number)

for number in in_range(10, 0, -3):
    print(number)

# Задание 3
#
# Создайте собственную реализацию итерируемого объекта, который можно использовать внутри цикла for-in.
# Также добавьте логику для извлечения элементов с использованием синтаксиса квадратных скобок.

print(
    '''
Task 3
    '''
)


class CustomIterable:
    '''Создайте собственную реализацию итерируемого объекта, который можно использовать внутри цикла for-in.
    Также добавьте логику для извлечения элементов с использованием синтаксиса квадратных скобок.'''

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.data):
            value = self.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.data[index]


print(
    "Using for-in loop:"
)
custom_iter = CustomIterable([1, 2, 3, 4, 5])

for item in custom_iter:
    print(item)

print(
    "\nAccessing with square brackets:"
)
print(custom_iter[0])
print(custom_iter[2])
print(custom_iter[-1])
