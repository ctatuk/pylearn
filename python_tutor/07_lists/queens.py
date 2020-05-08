def compare(pair1, pair2):
    return pair1[0] == pair2[0] \
           or pair1[1] == pair2[1] \
           or abs(pair1[0] - pair2[0]) == abs(pair1[1] - pair2[1])


def queens(l):
    '''
    Source https://pythontutor.ru/lessons/lists/problems/lists_queens/
    Condition
    It is known that 8 queens can be placed on an 8 × 8 board so that they do not beat each other.
    You have been given the arrangement of 8 queens on the board,
    determine if there is a pair of beating each other among them.
    The program receives eight pairs of numbers as an input,
    each number from 1 to 8 - coordinates of 8 queens. If the queens do not beat each other,
    print the word NO, otherwise print YES.
    '''
    for index in range(len(l) - 1):
        for i in range(index + 1, len(l)):
            print(l[index], l[i])
            print(compare(l[index], l[i]))


queens([(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)])
queens([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)])
