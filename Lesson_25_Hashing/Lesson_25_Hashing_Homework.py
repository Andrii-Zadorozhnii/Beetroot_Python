# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
# Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
# Визначте складність алгоритму та порівняйте його з бінарним пошуком

insert_list = [i for i in range(1, 101)]


def binary_search(search_list: list,
                  looking_number: int,
                  steps=0):
    if not search_list:
        return False, steps

    mid = len(search_list) // 2

    if search_list[mid] == looking_number:
        return True, steps + 1
    elif search_list[mid] < looking_number:
        return binary_search(search_list[mid + 1:],
                             looking_number,
                             steps + 1)
    else:
        return binary_search(search_list[:mid],
                             looking_number,
                             steps + 1)


found, step_count = binary_search(insert_list,
                                  5)


def fibonacci_search(arr, x):
    n = len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n:
        fib2, fib1 = fib1, fib
        fib = fib1 + fib2

    index = -1
    steps = 0

    while fib > 1:
        steps += 1
        i = min(index + fib2, n - 1)

        if arr[i] < x:
            fib, fib1, fib2 = fib1, fib2, fib1 - fib2
            index = i
        elif arr[i] > x:
            fib, fib1, fib2 = fib2, fib1 - fib2, fib2 - fib1
        else:
            return True, steps

    if fib1 and index < n and arr[index + 1] == x:
        return True, steps + 1

    return False, steps


found_fib, step_count_fib = fibonacci_search(insert_list,
                                             5)

print(
    f"Binary Search - Found: {found}, Steps for search: {step_count}"
)
print(
    f"Fibonacci Search - Found: {found_fib}, Steps for search: {step_count_fib}"
)
