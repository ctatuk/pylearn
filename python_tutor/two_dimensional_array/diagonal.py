def diagonal(n):
    '''Условие
    Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
    На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих
    к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.'''
    field = []
    for i in range(n):
        field.append(n * ['.'])
    #for row in field:
        #print(row)
    counter = 0
    for x in range(n):
        #print(x)
        for y in range(n):
            field[x][y]=y
            #field[x+1][y]=

            #print(y)
            if x == y:
                field[x][y]=0
            elif x > y and y < x:
                field[x][y] = x+1

    for row in field:
        print(row)

diagonal(5)

'''def shift(n):
    lst = []

    for i in range(n):
        # lst.append(lst.pop(0))
        #print(lst)#for i in range(steps):
        #lst.insert(0, lst.pop())
        #print(lst)

#shift(5)'''