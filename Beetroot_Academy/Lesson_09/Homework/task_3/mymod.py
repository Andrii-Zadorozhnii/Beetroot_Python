
# Создайте модуль Python под названием «mymod.py», который имеет три функции:

# Функция count_lines(name), которая считывает входной файл и подсчитывает количество строк в нем
def count_lines(name):
    with open(name,'r') as file:
        lines = len(file.readlines())
        return print(
            f'Lines in the file: {lines}'
        )

# Функция count_chars(name), которая считывает входной файл и подсчитывает количество символов в нем
def count_chars(name):
    with open(name,'r') as file:
        symbols = len(file.read())
        return print(
            f'Symbols in the file: {symbols}\n'
        )

# Функция test(name), которая вызывает обе функции подсчета с заданным входным именем файла.
def test(name):
    count_lines(name)
    count_chars(name)

print(
    'Result for Reading file'
)
test('reading_file.txt')
print(
    'Result from mymod.py file'
)
# Попробуйте запустить свой модуль сам по себе: например, test("mymod.py").
test('mymod.py')


# Переписываем код с использованием file.seek(0)

def count_lines_1(file):
    lines = len(file.readlines())
    return print(
        f'Lines in the file: {lines}'
    )

def count_chars_1(file):
    file.seek(0)
    symbols = len(file.read())
    return print(
        f'Symbols in the file: {symbols}\n'
    )

def test_1(name):
    with open(name, 'r') as file:
        count_lines_1(file)
        count_chars_1(file)

print(
    'Result for Reading file with file.seek(0)'
)
test_1('reading_file.txt')