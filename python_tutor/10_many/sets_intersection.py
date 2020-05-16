'''
    Source: https://pythontutor.ru/lessons/sets/problems/sets_intersection/
    Condition
    Two lists of numbers are given.
    Find all the numbers that appear in both the first and second list and print them in ascending order.
'''
def sets_intersection(n, m):
    print(sorted([x for x in n if x in m]))



sets_intersection({82, 54, 91, 100, 70, 33, 88, 14, 52, 48}, {10, 44, 77, 91, 43, 75, 25, 24, 5, 70})