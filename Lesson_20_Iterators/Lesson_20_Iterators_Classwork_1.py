class DivisibleBy3And7:
    def __init__(self, max_num):
        self.max_num = max_num
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.max_num:
            if self.start % 3 == 0 and self.start % 7 == 0:
                result = self.start
                self.start += 1
                return result
            self.start += 1
        raise StopIteration


def divisible_by_3_and_7_gen(max_num):
    for number in range(max_num):
        if number % 3 == 0 and number % 7 == 0:
            yield number


max_value = 10 ** 11
generator_expression = (x for x in range(max_value + 1) if x % 3 == 0 and x % 7 == 0)

import sys

max_value = 100000000000

iterator = DivisibleBy3And7(max_value)
print(
    "Iterator size:", sys.getsizeof(iterator)
)

generator_func = divisible_by_3_and_7_gen(max_value)
print(
    "Generator function size:", sys.getsizeof(generator_func)
)

print(
    "Generator expression size:", sys.getsizeof(generator_expression)
)
