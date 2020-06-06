def rook(x1, y1, x2, y2):
    '''
    Source https://pythontutor.ru/lessons/ifelse/problems/rook_move/
    Condition
    A chess rook moves horizontally or vertically. Given two different cells of a chessboard,
    determine whether the rook can get from the first cell to the second in one move.
    The program receives four numbers from 1 to 8 each, specifying the column number and row number,
    first for the first cell, then for the second cell.
    The program should output YES if the rook can be transferred to the second or NO otherwise from the first cell.
    '''
    for elem in x1, y1, x2, y2:
        print(elem)
        if elem < 1 or elem > 8:
            print('use numbers from 1 to 8')
            break


rook(0, 3, 4, 5)
