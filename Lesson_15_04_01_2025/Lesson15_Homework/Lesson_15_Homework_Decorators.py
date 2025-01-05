# Task 1
#
# Write a decorator that prints a function with arguments passed to it.
#
# NOTE! It should print the function, not the result of its execution!

def logger(func):
    def wrapper(*args):
        func(*args)

    return wrapper


@logger
def add(x, y):
    return print(
        f'Final result: {x}+{y}={x + y}'
    )


add(4, 5)


@logger
def square_all(*args):
    return print(
        [arg ** 2 for arg in args]
    )


square_all(2, 3, 4, 5, 6)


# Task 2
#
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def decorator(func):
        def wrapper(name: str):
            result = func(name)
            for word in words:
                result = result.replace(word, '*')
            return result

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


# Task 3
#
# Write a decorator 'arg_rules' that validates arguments passed to the function.
#
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

# If some of the rules ' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name: str):

            if not isinstance(name, type_):
                print(f"Аргумент не является типом {type_}")
                return False

            if len(name) > max_length:
                print(f"Аргумент превышает максимальную длину {max_length}")
                return False

            for symbol in contains:
                if symbol not in name:
                    print(f"Аргумент не содержит необходимый символ '{symbol}'")
                    return False

            return func(name)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
