# list = [1, 2, 3, 4, 5, 6]
# new_list = []
# # while len(list) > 0:
# #     new_list.append(list[-1])
# #     list.pop()
# #
# # print(new_list)
#
# new_list_2 = list[::-1]
# print(new_list_2)
#
# new_list_3 = []
# for i in range(len(list)):
#     new_list_3.append(list.pop())
#
# print(new_list_3)

from queue import Queue
from collections import deque

import random

random_list_1 = [random.randint(1, 999) for i in range(10)]
random_list_2 = [random.randint(1, 999) for i in range(50)]
random_list_3 = [random.randint(1, 999) for i in range(100)]


class Stack():
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()

    def size(self):
        return len(self.list)

    def __str__(self):
        result = '<Stack>\n'
        for index, item in enumerate(self.list):
            result += f'Index: {index + 1}, Value: {str(item)}\n'
        return result


stack = Stack()

for item in random_list_1:
    stack.push(item)
for item in random_list_2:
    stack.push(item)
for item in random_list_3:
    stack.push(item)

print(stack)
