numbers = [9, 2, 5, 7, 3, 6, 4]


def bubble_sort(some_list: list[int]) -> list[int]:
    '''
    Standard Bubble Sorting

    :param: some_list
    :return: sorted_list
    '''
    n = len(some_list)

    for i in range(n):
        for k in range(n - 1 - i):
            if some_list[k] > some_list[k + 1]:
                some_list[k], some_list[k + 1] = some_list[k + 1], some_list[k]

    return some_list


print(bubble_sort(numbers))


def selection_sort(some_list: list[int]) -> list[int]:
    '''
    standart sorting

    :param some_list: integer list
    :return: sorted list
    '''

    len_list = len(some_list)

    for i in range(len_list - 1, 0, -1):
        max_index = i

        for j in range(i):
            if some_list[j] > some_list[max_index]:
                max_index = j

        some_list[max_index], some_list[i] = some_list[i], some_list[max_index]

    return some_list


numbers_2 = [64, 25, 12, 22, 11]

print(selection_sort(numbers_2))
