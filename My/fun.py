def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print(arr[mid])
            return mid, steps
        elif arr[mid] < target:
            print(arr[mid])
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


# Пример использования
def array_list(number):
    counter = 0
    new_arr = []
    while counter <= number:
        new_arr.append(counter)
        counter += 1
    return new_arr


arr = array_list(9999)
# print(arr)

target = 9999

result, steps = binary_search(arr, target)

if result != -1:
    print(
        f"Элемент найден на индексе {result}. Количество шагов: {steps}"
    )
else:
    print(
        f"Элемент не найден. Количество шагов: {steps}"
    )


def bubble_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            steps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, steps


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, steps = bubble_sort(arr)

print(f"Отсортированный массив: {sorted_arr}")
print(f"Количество шагов: {steps}")
