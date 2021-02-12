'''
    Source: https://pythontutor.ru/lessons/sets/problems/number_of_unique/
    Condition
    A list of numbers is given. Determine how many different numbers there are in it.
'''
def number_of_unique(list_a):
    print(len(set(list_a)))

number_of_unique({1, 2, 3, 4, 5, 1, 3, 4, 2})