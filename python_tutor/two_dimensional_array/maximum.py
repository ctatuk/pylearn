
'''
    Source: https://pythontutor.ru/lessons/2d_arrays/problems/2d_max/
    Condition
    Find the indices of the first occurrence of the maximum element.
    Print two numbers: the row number and the column number,
    in which the largest element in the two-dimensional array is.
    If there are several such elements, then the one with the lower row number is displayed,
    and if the row numbers are equal, the one with the lower column number.
    The program receives the input sizes of the array n and m, then n lines of m numbers in each.
'''
def max_element(a_array):
    for row in a_array:
        print(row)
    a = a_array[0][0]
    x, y = 0, 0
    for n in range(len(a_array)):
        for m in range(len(a_array[n])):
            if a_array[n][m] > a:
                a = a_array[n][m]
                x, y = n + 1, m + 1
    print('max: ', a, 'coordinates: ', x, y)

max_element([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]])
