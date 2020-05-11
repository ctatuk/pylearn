def horse(x1, y1, x2, y2):
    '''
    Source https://pythontutor.ru/lessons/ifelse/problems/knight_move/
    Condition
    A chess horse moves with the letter “G” - two squares vertically in any direction and one square horizontally,
    or vice versa. Given two different checkerboard squares,
    determine if the knight can get from the first square to the second in one move.
    '''

    for elem in x1, y1, x2, y2:
        if elem < 1 or elem > 8:
            print('Please provide coordinates from 1 to 8')
            return

    x_distance = abs(x2 - x1)
    y_distance = abs(y2 - y1)

    if sorted([x_distance, y_distance]) == [1, 2]:
        print('Yes')
    else:
        print('No')


horse(5, 2, 4, 4)
horse(2, 8, 3, 7)
horse(2, 4, 2, 5)
horse(4, 7, 6, 6)
