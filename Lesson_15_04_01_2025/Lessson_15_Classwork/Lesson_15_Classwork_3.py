def first_decorator(func):
    def wrap():
        print('before')
        func()
        print('after')

    return wrap


def test():
    """test function docs"""
    print('inside test')


result = first_decorator(test)
print(result.__name__)

result()
