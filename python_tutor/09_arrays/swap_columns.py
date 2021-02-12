'''
    Source: https://pythontutor.ru/lessons/2d_arrays/problems/swap_columns/
    Condition
    A two-dimensional array and two numbers are given: i and j.
    Change the columns with numbers i and j in the array and print the result.
    The program receives the input the sizes of the array n and m,
    then the elements of the array, then the numbers i and j.
    Design the solution as a function swap_columns (a, i, j).
'''
def swap_columns(a, i, j):
    print('start: ')
    for row in a:
        print(row)
    for y in range(len(a[1])):
        for x in range(len(a)):
            if y == i:
                a[x][i], a[x][j] = a[x][j], a[x][i]
    print('end: ')
    for row in a:
        print(row)
swap_columns([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]], 0, 1)
