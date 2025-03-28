class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):

        try:
            self.file = open(self.filename, self.mode)
            print(
                "\nFile is open.\n"
            )
            return self.file


        except FileNotFoundError:
            print('File not found')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(exc_val)
        else:
            print(
                "\nFile is close.\n"
            )


with File('text.txt', 'w') as f:
    f.write(
        'Hello Dolly'
    )
    print(
        "\nFile rewrites.\n"
    )

with File('text.txt', 'r') as f:
    data = f.read()
    print(data)

from contextlib import contextmanager


@contextmanager
def file_context(filename):
    file = open(filename, 'w')
    print(
        "\nFile is open.\n"
    )
    try:
        yield file
    finally:
        file.close()
        print(
            "\nFile is close.\n"
        )


with file_context('text_2.txt') as f:
    f.write(
        'Hello Igor, I see you =)'
    )
    print(
        "\nFile rewrites.\n"
    )

with open('text_2.txt', 'r') as f_read:
    a = f_read.read()
    print(a)
