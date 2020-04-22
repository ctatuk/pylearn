def rainbow():
    i = 1
    for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
        print('#', i, ' color of rainbow is ', color, sep='')
        i += 1


'''   
Условие
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
'''


def factorial(num):
    fact = 1
    for i in range(1, num):
        fact = fact * i
        print(fact)


factorial(10)


def zero_counter(num_list):
    counter = 0
    num = len(num_list)
    indices = range(num)
    '''
    print(indices)
    print(list(indices))
    zip_list = list(zip(num_list, indices))
    print(zip_list)
    '''
    for i in zip(num_list, indices):
        if i[0] == 0:
            counter += 1
            print(i)


zero_counter([1, 0, 10, 30, 0, 7, 25, 0, 75])
