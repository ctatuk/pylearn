#Learning decorators
#Source https://nuancesprog.ru/p/1284/ Part1 and https://nuancesprog.ru/p/1287/ Part2

def three(operator=None):
    if operator is None:
        return 3
    else:
        return operator(3)


def five(operator):
    if operator is None:
        return 5
    else:
        return operator(5)


def plus(second_number):
    def inner(first_number):
        return first_number + second_number

    return inner


# Get it?
# five(plus(three()))
# five(plus(3)) -> def inner: return first_number + 3
# five(inner) -> inner(5) -> 5 + 3 -> 8

assert five(plus(three())) == 8

passed = False
#assert passed, 'Not passed'


def print_them_args(func):
    def the_name_of_this_one_doesnt_matter(*args):
        print("{} called with {}".format(func.__name__, [*args]))
        return func(*args)

    return the_name_of_this_one_doesnt_matter


@print_them_args
def add(a, b):
    return a + b


add(5, 8)
