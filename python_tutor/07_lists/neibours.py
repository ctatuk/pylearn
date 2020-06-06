def one_sign(d):
    '''
    Source https://pythontutor.ru/lessons/lists/problems/same_sign_neighbours/
    Condition
    A list of numbers is given. If it has two adjacent elements of the same sign, print these numbers.
    If there are no adjacent elements of the same sign, do not print anything.
    If there are several such pairs of neighbors, print the first pair.
    '''
    i = 0
    while d:
        if d[i] * d[i + 1] > 0:
            print(d[i], d[i + 1])
            break
        else:
            i += 1


one_sign([-4, 5, -2, -6, -4, 6, 6])
