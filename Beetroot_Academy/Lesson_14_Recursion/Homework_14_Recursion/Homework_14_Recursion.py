#############################################
# All tasks should be solved using recursion
#############################################

# Task 1
#
# from typing import Optional
# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
#     """
#     Returns  x ^ exp
#
#     >>> to_power(2, 3) == 8
#     True


#     >>> to_power(3.5, 2) == 12.25
#     True


#     >>> to_power(2, -1)
#     ValueError: This function works only with exp > 0.
#     """®
#     pass
def to_power(x, exp):
    if exp <= 0:
        raise ValueError
    if exp == 1:
        return x
    return x * to_power(x, exp - 1)


print(to_power(2, 3))
try:
    to_power(2, -1)
except ValueError:
    print('ValueError: This function works only with exp > 0.')


# Task 2
#
# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     """
#     Checks if input string is Palindrome
#     >>> is_palindrome('mom')
#     True
#
#     >>> is_palindrome('sassas')
#     True
#
#     >>> is_palindrome('o')
#     True
#     """
#     pass

def is_palindrome(looking_str, index=0):
    if index >= len(looking_str) // 2:
        return True
    if looking_str[index] != looking_str[-1 - index]:
        return False
    return is_palindrome(looking_str, index + 1)


is_palindrome('mom')

is_palindrome('sassas')

is_palindrome('o')


# Task 4
#
# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     >>> reverse("hello") == "olleh"
#     True
#     >>> reverse("o") == "o"
#     True

def reverse(input_str):
    return input_str[::-1]


print(reverse("hello"))

reverse("o")
