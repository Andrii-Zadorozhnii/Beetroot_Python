# Count
from itertools import count

from Lesson_20_Iterators.Lesson_20_Iterators_Classwork_1 import max_value

counter = count(0)
list1 = ["A", "B", "C"]
list2 = ["a", "b", "c"]

result = [(next(counter), x, y) for x, y in zip(list1, list2)]
print(result)

# Chain

from itertools import chain

list1 = ["A", "B", "C"]
list2 = ["a", "b", "c"]

chained = chain(list1, list2)

result = [next(chained) for _ in range(len(list1) + len(list2))]
print(result)

# Compress

from itertools import compress
import random

list1 = [random.randint(1, 15) for _ in range(20)]
list2 = [random.choice([0, 1]) for _ in range(20)]

compressed = compress(list1, list2)

result = []
while True:
    try:
        result.append(next(compressed))
    except StopIteration:
        break

print("list1:", list1)
print("list2:", list2)
print("result:", result)

# Takewhile

from itertools import takewhile

a_list = [(1, "B"), (2, "C"), (3, "A"), (4, "D"), (4, "D")]

filtered = list(takewhile(lambda x: x[0] < 3, a_list))

print(filtered)

# StartMap

from itertools import starmap

# Данные
a_list = [[1, 2, 3], [4, 5, 6, 7, 8, 89, 7, 6, 4, 3, 1, 3, 2], [0]]


def c_max(iterable):
    max_value = iterable[0]
    for item in iterable:
        if item > max_value:
            max_value = item
    return max_value


max_values = list(starmap(c_max, [(sublist,) for sublist in a_list]))

print(max_values)

# Product

from itertools import product

products = product('AB', "ab", 'ef')

result = []
while True:
    try:
        result.append(next(products))
    except StopIteration:
        break

print(result)

# Combination

from itertools import combinations

combinations_iter = combinations("ABCDE", 3)

result = []
while True:
    try:
        result.append(next(combinations_iter))
    except StopIteration:
        break

print(result)

# Permutation

from itertools import permutations

permutations_iter = permutations("ABCDE", 3)

result = []
while True:
    try:
        result.append(next(permutations_iter))
    except StopIteration:
        break

print(result)
