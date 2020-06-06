def snowflakes(n):
    '''
    Source https://pythontutor.ru/lessons/2d_arrays/problems/snowflake/
    Condition
    Given an odd number n. Create a two-dimensional array of n × n elements,
    filling it with characters "." (each element of the array is a string of one character).
    Then fill in with the characters "*" the middle row of the array, the middle column of the array,
    the main diagonal and the side diagonal. As a result, units in the array should form an asterisk image.
    Display the resulting array on the screen, separating the elements of the array with spaces.
    '''
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
                field[x][y] = 'X'

    for row in field:
        print(row)


snowflakes(30)