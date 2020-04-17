def test_chess_cell(x, y):
    # False if cell white, True if cell black
    if x % 2 != 0 and y % 2 != 0:
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


compare_cell(1, 4, 5, 7)
