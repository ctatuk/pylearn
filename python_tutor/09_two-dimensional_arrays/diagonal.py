def diagonal(n):
    '''
    Source https://pythontutor.ru/lessons/2d_arrays/problems/diagonals/
    Condition
    Given the number n. Create an n × n array and fill it in accordance with the following rule.
    The numbers 0 should be written on the main diagonal. On the two diagonals adjacent to the main, the numbers 1.
    On the next two diagonals, the numbers 2, etc.
    '''
    matrix = []

    comp_list = [x for x in range(n)]

    for i in range(n):
        matrix.append([x for x in comp_list])
        comp_list.pop()
        comp_list.insert(0, i + 1)

    print('Matrix:')
    for row in matrix:
        print(row)


def diagonal2(n):
    '''
    Source https://pythontutor.ru/lessons/2d_arrays/problems/diagonals/
    Condition
    Given the number n. Create an n × n array and fill it in accordance with the following rule.
    The numbers 0 should be written on the main diagonal. On the two diagonals adjacent to the main, the numbers 1.
    On the next two diagonals, the numbers 2, etc.
    '''
    matrix = []
    for i in range(n):
        matrix.append(n * [''])

    for y in range(n):
        for x in range(n):
            matrix[y][x] = abs(y - x)
    for row in matrix:
        print(row)


def diagonal3(n):
    '''
    Source https://pythontutor.ru/lessons/2d_arrays/problems/diagonals/
    Condition
    Given the number n. Create an n × n array and fill it in accordance with the following rule.
    The numbers 0 should be written on the main diagonal. On the two diagonals adjacent to the main, the numbers 1.
    On the next two diagonals, the numbers 2, etc.
    '''
    matrix = [[i for i in range(n - 1, 0, -1)][n - i - 1:n] + [0] + [i for i in range(1, n)][:n - i - 1] for i in range(n)]
    for row in matrix:
        print(row)


def diagonal4(n):
    '''
    Source https://pythontutor.ru/lessons/2d_arrays/problems/diagonals/
    Condition
    Given the number n. Create an n × n array and fill it in accordance with the following rule.
    The numbers 0 should be written on the main diagonal. On the two diagonals adjacent to the main, the numbers 1.
    On the next two diagonals, the numbers 2, etc.
    '''
    matrix = [[abs(j - i) for j in range(n)] for i in range(n)]
    for row in matrix:
        print(row)


diagonal(5)
diagonal2(5)
diagonal3(5)
diagonal4(5)
