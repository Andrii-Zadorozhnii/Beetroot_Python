def test_1(param):
    print(f'I\'m a function test_1, print {param}')


def test():
    var_a = 19

    def low():
        print("I'm a function low")

    return low
    # nonlocal var_a
    # var_a = 1919
    # print('world', word, 'var_a:', var_a, 'global_a:', global_a)
    #
    # if it.isdigit():
    #     return 'N'
    # return it.lower()

    res = ''
    # for i in word:
    #     res += low(i)
    # return res


#     low('')
#     print("var_a, enclosed:  ", var_a)
#
#
# global_a = 1000

# print(test('12TYj8'))

# asd = test_1
# asd()
# test_1()
var_f = test()

var_f()

test()
