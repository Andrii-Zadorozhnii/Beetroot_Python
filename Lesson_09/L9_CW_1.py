"""
Задача 1.
Створити файл, в ньому – оператор print, що виводить:
назву файлу
атрибут __name__
Запустити файл на виконання, а також імпортувати його з іншого файлу. Як зміниться атрибут __name__ ?
Задача 2.
Файл з задачі 1 змінити його таким чином, щоб оператор print виводив інформацію лише в тому випадку, 
коли виконується запуск даного файлу, при імпорті з іншого файлу -  print не повинен спрацьовувати.
Задача 3.
Створіть у файлі 1 (задача 2) кілька простих функцій.
Імпортуйте даний модуль у інший (файл 2) з alias (придумайте самі).
Імпортуйте одну з функцій в файл 2 з alias (придумайте самі).
Спробуйте запустити фунцію 2-ма способами: через alias модуля, та через свій alias.
Задача 4.
Створіть файл random.py, в ньому функцію randint(яка виводить якесь привітання). Імпортуйте його, перевірте,
як веде себе знайома вам функція  random. Randint
"""
import random
import print_task_1 as printt
from print_task_1 import add as a
from print_task_1 import minus as b
print(a(1,2))
print(b(3,1))
print(printt.add(1,3))
random.randint()