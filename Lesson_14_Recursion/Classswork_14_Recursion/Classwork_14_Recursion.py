# def calcualtion(n):
#     print(n)
#     if n == 1:
#         print(1)
#         # return 1
#     else:
#         return calcualtion(n - 1)
#         print(n)
#
#
# calcualtion(5)


def calcul2(n):
    if n == 1:
        print(1)
        return 1
    print(n)
    # return calcul2(n - 1)
    calcul2(n - 1)
    print(n)


calcul2(5)


def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)


print(fib(6))
