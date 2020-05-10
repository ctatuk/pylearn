'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/series_2/
    Given two integers A and B. Print all numbers from A to B inclusive,
    in ascending order if A < B, or in descending order otherwise.
'''
def ranks_two(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)
ranks_two(10, 0)