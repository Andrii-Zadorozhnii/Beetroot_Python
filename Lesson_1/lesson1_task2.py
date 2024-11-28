print('Homework 1. Task 2')

print("""
Create a python program named "task2", and use the built-in function 'print' in it several times.
Try to pass "sep", "end" params and pass several parameters separated by commas.
Also, provide a comment text above each print statement, mentioned above,
with the expected output after execution of the particular print statement.

(Ex.
# 'hello world'
print("hello world")
)
""")



# 'hello world'
print(
    "hello", "world"
    )

# 'hello\tworld' (tab character between words)
print(
    "hello", "world",
    sep="\t"
    )

# 'hello---world' (--- separator between the words)
print(
    "hello", "world",
    sep="---"
    )

# 'hello world' followed by a newline (default end="\n")
print(
    "hello", "world",
    sep=" ",
    end="\n"
    )

# 'hello world' (printed without space between words)
print(
    "hello", "world",
    sep=""
    )

# '1\n5\nhello\nworld' (each element separated by a newline, specified by sep="\n")
print(
    1, 5, "hello", "world",
    sep=" \n"
    )