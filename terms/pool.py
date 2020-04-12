def yasha_in_the_pool(n, m, x, y):
    # s - минимальное расстояние до бортика

    if x < 0.5 * n:
        s = x
        print(s)
    if y < 0.5 * m:
        s = y
        print(s)
    if x > 0.5 * n:
        s = n - x
        print(s)
    if y > 0.5 * m:
        s = m - y
        print(s)


yasha_in_the_pool(10, 86, 3, 43)
