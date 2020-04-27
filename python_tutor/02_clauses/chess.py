def test_chess_cell(x, y):
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/chess_board/
    Condition
    Two checkerboard squares are set. If they are painted the same color,
    print the word YES, and if in different colors - then NO.
    The program receives four numbers from 1 to 8 each, specifying the column number and
      line number first for the first cell, then for the second cell.
    """
    if x % 2 != 0 and y % 2 != 0:  # False if cell white, True if cell black
        return True
    if x % 2 != 0 and y % 2 == 0:
        return False
    if x % 2 == 0 and y % 2 != 0:
        return False
    else:
        return True


def compare_cell(x1, y1, x2, y2):
    cell1 = test_chess_cell(x1, y1)
    cell2 = test_chess_cell(x2, y2)
    if cell1 == cell2:
        print('The cells color is similar')
    else:
        print('The cells color is different')


compare_cell(1, 4, 5, 8)
