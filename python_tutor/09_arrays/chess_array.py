'''
    Source: https://pythontutor.ru/lessons/2d_arrays/problems/diagonals/
    Condition
    Given the number n. Create an n × n array and fill it in accordance with the following rule.
    The numbers 0 should be written on the main diagonal.
    On the two diagonals adjacent to the main, the numbers 1. On the next two diagonals, numbers 2, etc.
'''
def diagonal_array(n):
    if n % 2 == 0:
        n += 1
    field = []
    for i in range(n):
        field.append(n * ['.'])
    for x in range(n):
        for y in range(n):
            if x == y:
                field[x][y] = 0
            else:
                field[x][y] = abs(x - y)
    for row in field:
        print(row)
    print()

#diagonal_array(9)

def diagonal_1(n):
    a = [[i for i in range(n - 1, 0, -1)][n - i - 1:n] + [0] + [i for i in range(1, n)][:n - i - 1] for i in range(n)]
    for row in a:
        print(row)
diagonal_1(5)