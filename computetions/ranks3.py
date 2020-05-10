'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/series_3/
    Given two integers A and B, A> B.
    Print all odd numbers from A to B inclusive, in descending order.
    In this task, you can do without the if statement.
'''
def rank_three(a, b):
    if a <= b:
        print('a должно быть больше b')
    if a % 2 == 0:
        a = a - 1
    for i in range(a, b - 1, -2):
        print(i)
rank_three(11, 1)
