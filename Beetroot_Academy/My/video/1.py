x = 10
print(x)


def update_x():
    global x
    x = 20


update_x()
print(x)
