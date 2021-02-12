'''
    Source: https://pythontutor.ru/lessons/sets/problems/occurs_before/
    Condition
    The input string contains a sequence of numbers separated by spaces.
    For each number print the word YES (in a separate line)
    if this number was previously encountered in the sequence or NO if it did not.
'''
def occurs_before(n_list):
    a = n_list.split()
    result = ['yes' if x in a[:i] else 'no' for i, x in enumerate(a)]
    print(result)


occurs_before('1 2 3 2 3 4')