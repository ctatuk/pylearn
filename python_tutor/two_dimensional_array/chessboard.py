def chessboard(n):
    '''
    Условие
    Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "."
    и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
    :param n:
    :return:
    '''
    field = []
    for i in range(n):
        field.append(n * ['*'])
    for y in range(n):
        for x in range(n):
            if y%2 == 0 and x%2 == 0 or y%2 == 1 and x%2==1:
                field[x][y] = '.'
    for row in field:
        print(row)


chessboard(8)