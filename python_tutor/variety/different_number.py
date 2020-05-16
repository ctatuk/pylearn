def different_number(n):
    '''
    Условие
    Дан список чисел. Определите, сколько в нем встречается различных чисел.
    '''
    print(len(set(n)))


different_number({1, 2, 3, 4, 8, 2, 1})