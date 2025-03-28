# Task 1
#
# Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.
print(
    '\nTask_1\n'
)


class Stack:
    def __init__(self, list):
        self.list = list
        print(
            f'Inserted list: {self.list}\n'
        )
        # print(self.list)

    def list_reversing(self):
        new_list = self.list[::- 1]
        # print(new_list)
        print(
            f'Reversed list: {new_list}'
        )
        return new_list


list_1 = [1, 2, 3, 4, 5, 6, 7]
# print(list_1)
stack_1 = Stack(list_1)
print((stack_1.list_reversing()))

# Task 2
#
# Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."
print(
    '\nTask_2\n'
)
brackets = '([]{}()())'


# brackets.split()


# class Bracket_Checker:
#     def __init__(self, string):
#         self.string = string
#         (self.open_bracket,
#          self.close_bracket,
#          self.open_parentheses,
#          self.close_parentheses,
#          self.open_curly_brackets,
#          self.close_curly_brackets) = (
#             0, 0, 0, 0, 0, 0)
#         self.check_brackets()
#
#     def check_brackets(self):
#         for i in brackets:
#
#             if i == "(":
#                 self.open_bracket += 1
#             elif i == ")":
#                 self.close_bracket += 1
#             elif i == '[':
#                 self.open_parentheses += 1
#             elif i == "]":
#                 self.close_parentheses += 1
#             elif i == '{':
#                 self.open_curly_brackets += 1
#             elif i == '}':
#                 self.close_curly_brackets += 1
#             else:
#                 print(
#                     f'No any brackets'
#                 )
#         if self.open_bracket != self.close_bracket:
#             print(
#                 f'Brackets is not correct\nOpen brackets: {self.open_bracket}\nClose brackets: {self.close_bracket}'
#
#             )
#         elif self.open_parentheses != self.close_parentheses:
#             print(
#                 f'Parentheses is not correct\nOpen brackets: {self.open_parentheses}\nClose parentheses: {self.close_parentheses}'
#             )
#         elif self.open_curly_brackets != self.close_curly_brackets:
#             print(
#                 f'Curly Brackets is not correct\nOpen curly brackets: {self.open_curly_brackets}\nClose curly brackets: {self.close_curly_brackets}'
#             )
#         else:
#             print(
#                 f'All brackets is correct'
#             )

class Bracket_Checker:
    def __init__(self, string):
        self.string = string

    def check(self):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in self.string:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != pairs[char]:
                    return "Not Balanced"
                stack.pop()

        return "Balanced" if not stack else "Not Balanced"


checker = Bracket_Checker(brackets)

print(checker.check())

# Task 3
#
# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message
print(
    '\nTask_3\n'
)


class Stack_Checker:
    def __init__(self, list):
        self.list = list
        print(
            f'Initialize list: {self.list}'
        )

    def get_from_stack(self, value):
        '''Get data from list'''

        if value in self.list:
            self.list.remove(value)
            print(
                f'Get item from list: {value}\nList remained: {self.list}'

            )
            return value
        else:
            raise ValueError(f"'{value}' not in list")


stack = ['hello', 'world', "!!!"]

result = Stack_Checker(stack)

result.get_from_stack('hello')
result.get_from_stack('!!!')
result.get_from_stack('hell')
