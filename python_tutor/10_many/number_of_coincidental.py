'''
    Source: https://pythontutor.ru/lessons/sets/problems/number_of_coincidental/
    Condition
    Two lists of numbers are given.
    Calculate how many numbers are contained simultaneously in both the first list and the second.
    Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
'''
def number_of_coincidental(a, b):
    print(len(a.intersection(b)))

number_of_coincidental({1, 3, 2, 4, 7, 5}, {4, 3, 2, 0})