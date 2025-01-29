import time
import random

list_1 = []


def random_list(numbers):
    return_list = []
    for i in range(numbers):
        return_list.append(random.randint(1, numbers))
        # print(return_list)
    return return_list


list_1 = random_list(100)
print(list_1)


def min_funct_n2(lst):
    start_time = time.time()
    min_value = lst[0]

    for i in lst:
        print(f'Цикл i: {i}')
        for j in lst:
            print(f'Цикл j. i:{i}, j:{j}')
            if i < j:
                result = i
                if result <= min_value:
                    min_value = result
                print(f'min_value: {min_value}')

    end_time = time.time()
    total_time = end_time - start_time
    print(
        f"Time for min_funct_n2: {total_time} seconds"
    )
    print(
        f"Minimum value (O(n^2)): {min_value}"
    )
    return min_value


def min_funct_n(lst):
    start_time = time.time()
    min_value = lst[0]

    for i in lst:
        if i < min_value:
            min_value = i

    end_time = time.time()
    total_time = end_time - start_time
    print(
        f"Time for min_funct_n: {total_time} seconds"
    )
    print(
        f"Minimum value (O(n)): {min_value}"
    )
    return min_value


min_funct_n2(list_1)
min_funct_n(list_1)
