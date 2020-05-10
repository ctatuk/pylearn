'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/series_1/
    Condition
    Two integers A and B are given (with A ≤ B).
    Print all numbers from A to B inclusive.
'''
def rank_one(a, b):
    if a > b:
        print('a должно быть меньше или равно b')
        return
    num_list = []
    for i in range(a, b + 1):
        num_list.append(i)
    print(num_list)
rank_one(-3, 14)
