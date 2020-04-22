def find_second_f(array, pattern):
    # если буква f не встречается
    if array.count(pattern) == 0:
        print(-2)
    # если буква f встречается только однажды
    elif array.count(pattern) == 1:
        print(-1)
    # ищем букву f в строке начиная от следующего символа после 1 буквы f
    else:
        y = array.find(pattern, array.find(pattern) + 1)
        print(y, array[y])


# find_second_f('aldsfkaofdaiur', 'f')


def cycle_while(a):
    n = 0

    while a[n] != 0:
        if a[n] == ' ':
            print('Встретился пробел перед', a[:n])
            break
        n += 1

    else:
        print('Ни одного пробела не встретилось')


cycle_while('wawfsfse fessfesf')
