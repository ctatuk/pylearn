def cycle_while(a):
    n = 0
    while a[n] != 0:
        if a[n] == ' ':
            print('We found space', a[:n])
            break
        n += 1
    else:
        print('No spaces in text')


cycle_while('wawfsfse fessfesf')