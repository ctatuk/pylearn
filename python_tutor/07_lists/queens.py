def compare(pair1, pair2):

def queens(l):
    '''
    It is known that 8 queens can be placed on an 8 × 8 board so that they do not beat each other.
    You have been given the arrangement of 8 queens on the board,
     determine if there is a pair of beating each other among them.
    The program receives eight pairs of numbers as an input,
     each number from 1 to 8 - coordinates of 8 queens.
    If the queens do not beat each other, print the word NO, otherwise print YES.
    '''
    for index in range(len(l) - 1):
        for i in range(index + 1, len(l)):

        if x == l[index+1][0] or y == l[index+1][1] or abs(x - l[index + 1][0]) == abs(y - l[index + 1][1




queens([(1, 8), (2, 7), (6, 3), (4, 5), (5, 4), (3, 6), (7, 2), (8, 1)])


