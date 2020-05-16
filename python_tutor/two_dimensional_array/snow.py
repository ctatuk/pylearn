def snowflakes(n):
    if n % 2 == 0:
        n += 1
    field = []
    for i in range(n):
        field.append(n * ['.'])
    for row in field:
        print(row)
    print()
    print(n/2//2)
    for x in range(n):
        for y in range(n):
            if x == y or x == n // 2 or y == n // 2 or y == n - x - 1 \
                    or y == n - 3 and 0 <= x <= 2 \
                    or y == n - 3 and n - 2 <= x <= n \
                    or x == n - 3 and 0 <= y <= 2 \
                    or x == n - 3 and n - 2 <= y <= n \
                    or y == 2 and 0 <= x <= 2 \
                    or y == 2 and n - 2 <= x <= n \
                    or x == 2 and 0 <= y <= 2 \
                    or x == 2 and n - 2 <= y <= n:
                field[x][y] = '*'

    for row in field:
        print(row)


snowflakes(10)
