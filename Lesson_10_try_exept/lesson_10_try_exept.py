# Задача 1.
# Добийтесь отримання виключень типу TypeError, IndexError

number = "10"


def func_type_error_1():
    try:
        a = number + 2
    except TypeError:
        print(
            'TypeError'
        )

def func_index_error_2():
    try:
        print(number[10])
    except IndexError:
        print(
            'IndexError'
        )

func_type_error_1()
func_index_error_2()

# Задача 2.
# Обробіть виключення ZeroDivisionError, видайте повідомлення про некоректну операцію.

def func_zerro_dev(number):
    try :
        b = int(number) / 0
    except ZeroDivisionError:
        print(
            f'Incorrect operation, error: {ZeroDivisionError}'
        )

func_zerro_dev(number)

# Задача 3.
# Що буде, якщо в програмі (для задачі 2), в try виконати код '2' + 2

def func_zerro_dev_2():
    try :
        b = "2" + 2
    except ZeroDivisionError:
        print(
            f'Incorrect operation, error: {ZeroDivisionError}'
        )

func_zerro_dev_2() # Result is TypeError


# Задача 4 Обробіть виключення типу ZeroDivisionError, TypeError, IndexError в одному блоці

def func_exept_mix():
    try:
        a = "hello"
        b = a / 2
    except (ZeroDivisionError, TypeError, IndexError):
        print(
            f'Some of errors: ZeroDivisionError, TypeError, IndexError =) '
        )

func_exept_mix()

# Задача 5.
#  те саме, що в задачі 4, лише на кожен тип помилки – окремий except.

def func_exept_mix_2():
    try:
        a = "hello"
        b = a / 2
    except (ZeroDivisionError):
        print(
            f'Errors: ZeroDivisionError =) '
        )
    except (TypeError):
        print(
            f'Errors TypeError =) '
        )
    except (IndexError):
        print(
            f'Errors: IndexError =) '
        )

func_exept_mix_2()

# Задача 6.
# реалізуйте обробку для всіх класів виключень.

def func_check_all(something):
    try:
        raise(something)
    except Exception:
        print(
            'Some error'
        )


func_check_all("b")



# Задача 7.
# При якій умові виконається другий except ?
#  try:
#   1 / 0
#  except ZeroDivisionError:
#   print(1)
#  except ZeroDivisionError:
#   print(2)

def some_some():
    try:
        1 / 0
    except ZeroDivisionError:
        print(1)
    except IndexError:
        print(2)

some_some()

# Задача 8.
# Реалізуйте логіку роботи з кількома except для різних класів помилок, та блоком else. Коли виконується else ?

def some_exept():
    try:
        a = 1 / 1
    except ZeroDivisionError:
        print(
            'Delinting on 0'
        )
    except TypeError:
        print(
            'Input type error'
        )
    except IndexError:
        print(
            'some index error'
        )
    else:
        print(
            f'Final result is: {a}'
        )
    finally:
        print(
            "Calculation completed... "
        )

some_exept()

# Задача 9. В блоці try викиньте виключення з головним класом Exception, передайте кілька паратетрів.
# В except обробіть це виключення, виведіть параметри.

def func_try_exept():
    try:
        raise Exception("hello", 'world')
    except Exception as s:

        a, b = s.args
        print(
            f'Argument a is: {a.title()}')
        print(
            f'Argument b is :{b.title()}')

func_try_exept()


# Задача 10. Реалізуйте варіанти з finally:
# коли код працює нормально
# коли спрацьовує виключення і ви його ловите
# коли спрацьовує виключення і ви його пропускаєте
# Примітка: except та finally повинні повертати return з різними значеннями. Проаналізуйте, чи все коректно відпрацювало.

def funct_finally():
    try:
        a = 1 + 1
    finally:
        print(
            'All ok'
        )

funct_finally()