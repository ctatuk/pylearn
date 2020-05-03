def one_sign(d):
    i = 0
    while d:
        if d[i] * d[i + 1] > 0:
            print(d[i], d[i + 1])
            break
        else:
            i += 1


one_sign([-4, 5, -2, -6, -4, 6, 6])
