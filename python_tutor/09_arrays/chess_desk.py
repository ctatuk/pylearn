'''
    Source: https://pythontutor.ru/lessons/2d_arrays/problems/chessboard/
    Condition
    Two numbers n and m are given. Create a two-dimensional
    n × m array and fill it with "." and "*" in a checkerboard pattern.
    There should be a dot in the upper left corner.
'''


def chess_desk(n, m):
    matrix = [['*' for j in range(m)] for i in range(n)]
    #matrix = []
    #for i in range(n):
    #        matrix.append(['*'] * m)
    #for row in matrix:
    #    print(row)
    for x in range(n):
        for y in range(m):
            if x % 2 != 0 and y % 2 != 0 or x % 2 == 0 and y % 2 == 0:
                matrix[x][y] = '.'
    for row in matrix:
        print(row)
chess_desk(3, 4)
