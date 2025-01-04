print(
    f'\nHomework 13 - Assign function to variable'
)

# Task 1
#
# Write a Python program to detect the number of local variables declared in a function.

print(
    '\n_____ Task 1 ______\n'
)


def arguments_counter(*args):
    print(
        f'Total arguments in functions is: {len(args)}'
    )


arguments_counter(1, 2, 3, "hello", 5, 6, "a", 1, 3, 5, 6, "nbgh", 7, 3)

# Task 2
#
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

print(
    '\n_____ Task 2 ______\n'
)


def print_text(some_text):
    print(
        f'It is the text from first function: {some_text}'
    )


def second_function(function, function_argument):
    function(function_argument)
    print(
        'This is a text from second function'
    )


second_function(print_text, 'hello')

# Task 3
#
# Write a function called "choose_func" which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one
#
#
# def choose_func(nums: list, func1, func2):
#     pass
#
#
# # Assertions
#
# nums1 = [1, 2, 3, 4, 5]
#
# nums2 = [1, -2, 3, -4, 5]
#
#
# def square_nums(nums):
#     return [num ** 2 for num in nums]
#
#
# def remove_negatives(nums):
#     return [num for num in nums if num > 0]
#
#
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
#
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


print(
    '\n_____ Task 3 ______\n'
)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    if any(number < 0 for number in nums):  # Проверяем, есть ли отрицательные числа
        return print(func2(nums))
    else:
        return print(func1(nums))


choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)
