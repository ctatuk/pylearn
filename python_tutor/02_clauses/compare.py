def compare_digits(a, b, c):
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/minimum3/
    Condition
    Three integers are given. Print the value of the smallest of them.
    """
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)


compare_digits(4.6, 7, 2)
