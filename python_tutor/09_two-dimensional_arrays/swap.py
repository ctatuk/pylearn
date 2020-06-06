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
