# Task 1
#
# Extend UnsortedList
#
# Implement append, index, pop, insert methods for UnsortedList.
# Also implement a slice method, which will take two parameters 'start' and 'stop', and return a copy of the list starting at the position and going up to but not including the stop position.


class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.append(value)

    def index(self, value):
        try:
            return self.items.index(value)
        except ValueError:
            return -1

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def insert(self, index, value):
        self.items.insert(index,
                          value)

    def slice(self, start, stop):
        return self.items[start:stop]

    def __repr__(self):
        return str(self.items)


# Testing the UnsortedList class
unsorted_list = UnsortedList()
unsorted_list.append(10)
unsorted_list.append(20)
unsorted_list.append(30)
unsorted_list.insert(1, 15)
print(
    "List after insertion:", unsorted_list
)

print(
    "Index of 20:", unsorted_list.index(20)
)
print(
    "Pop last item:", unsorted_list.pop()
)
print(
    "List after pop:", unsorted_list
)

print(
    "Slice from index 0 to 2:", unsorted_list.slice(0, 2)
)


# Task 2
#
# Implement a stack using a singly linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def __repr__(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.value)
            current = current.next
        return "->".join(map(str, elements))


# Testing the Stack class
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(
    f"Stack: {stack}"
)

print(
    f"Peek: {stack.peek()}"
)
print(
    f"Pop: {stack.pop()}"
)
print(
    f"Stack after pop: {stack}"
)


# Task 3
#
# Implement a queue using a singly linked list.

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def __repr__(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return "->".join(map(str, elements))


# Testing the Queue class
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(
    f"Queue: {queue}"
)

print(
    f"Peek: {queue.peek()}")

print(
    f"Dequeue: {queue.dequeue()}"
)
print(
    f"Queue after dequeue: {queue}"
)
