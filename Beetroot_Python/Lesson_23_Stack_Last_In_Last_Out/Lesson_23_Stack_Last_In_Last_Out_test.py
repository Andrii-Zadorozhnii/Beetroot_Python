class SimpleStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def __repr__(self):
        return f"Top->{self.stack}<-Bottom)"


s = SimpleStack()
s.push(1)
s.push(2)
s.push(3)
print(s)

s.pop()
print(s)

s.push(4)
print(s)

s.push(2)
print(s)

s.pop()
s.pop()
s.pop()
s.pop()
print(s)
