'''
    Source: https://pythontutor.ru/lessons/2d_arrays/problems/secondary_diagonal/
    Condition
    Given the number n. Create an n × n array and fill it in accordance with the following rule:
    The numbers on the diagonal going from the upper right to the lower left corner are 1.
    The numbers above this diagonal are 0.
    The numbers below this diagonal are 2.
    Display the resulting array. Separate numbers in a line with one space.
'''
def diagonal_two(n):
    if n % 2 == 0:
        n += 1
    array = []
    for i in range(n):
        array.append(n * ['.'])
    for x in range(n):
        for y in range(n):
            if y == n - x - 1:
                array[x][y] = 1
            elif y > n - x - 1:
                array[x][y] = 2
            else:
                array[x][y] = 0
    for row in array:
        print(row)
diagonal_two(5)
