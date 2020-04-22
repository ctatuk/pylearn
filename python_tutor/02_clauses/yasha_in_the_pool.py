# Yasha is in the pool
# Pool size is M x N
# x will be distance from left side of the pool
# y will be distance rom the top side of the pool

def where_should_i_swim_v1(M, N, x, y):
    if M < 0 or N < 0:
        print("Looks like this is not a pool. Puzzling...")
        return
    if x > M or x < 0 or y > N or y < 0:
        print("Looks like I'm already out! Hurray")
        return

    x_from_right = M - x
    y_from_bottom = N - y
    if x <= x_from_right and y <= y_from_bottom and x <= y:
        print("I need to swim left!")
        return x
    if x <= x_from_right and y <= y_from_bottom and x >= y:
        print("I need to swim up!")
        return y
    if x_from_right < y_from_bottom:
        print("I need to swim right!")
        return x_from_right
    print("I guess I have no other choice but to swim down!")
    return y_from_bottom


def where_should_i_swim_v2(M, N, x, y):
    if M < 0 or N < 0:
        print("Looks like this is not a pool. Puzzling...")
        return
    if x > M or x < 0 or y > N or y < 0:
        print("Looks like I'm already out! Hurray")
        return
    x_from_right = M - x
    y_from_bottom = N - y

    if x <= x_from_right and x <= y <= y_from_bottom:
        print("I need to swim left!")
        return x
    # X is not the smallest
    if x_from_right <= y <= y_from_bottom:
        print("I need to swim right!")
        return x_from_right
    # X is not the smallest and x_from_bottom is also not the smallest
    if y <= y_from_bottom:
        print("I need to swim up!")
        return y
    print("I guess I have no other choice but to swim down!")
    return y_from_bottom


def where_should_i_swim_v3(M, N, x, y):
    if M < 0 or N < 0:
        print("Looks like this is not a pool. Puzzling...")
        return
    if x > M or x < 0 or y > N or y < 0:
        print("Looks like I'm already out! Hurray")
        return
    x_from_right = M - x
    y_from_bottom = N - y

    minimal_distance = -1

    if x <= x_from_right and x <= y <= y_from_bottom:
        print("I need to swim left!")
        minimal_distance = x
    # X is not the smallest
    elif x_from_right <= y <= y_from_bottom:
        print("I need to swim right!")
        minimal_distance = x_from_right
    # X is not the smallest and x_from_bottom is also not the smallest
    elif y <= y_from_bottom:
        print("I need to swim up!")
        minimal_distance = y
    else:
        print("I guess I have no other choice but to swim down!")
        minimal_distance = y_from_bottom
    return minimal_distance


def where_should_i_swim_v4(M, N, x, y):
    if M < 0 or N < 0:
        print("Looks like this is not a pool. Puzzling...")
        return
    if x > M or x < 0 or y > N or y < 0:
        print("Looks like I'm already out! Hurray")
        return

    return min(x, y, M - x, N - y)


def where_should_i_swim_v5(n, m, x, y):
    # s - минимальное расстояние до бортика
    if x < 0.5 * n:
        s = x
        return s
    if y < 0.5 * m:
        s = y
        return s
    if x > 0.5 * n:
        s = n - x
        return s
    if y > 0.5 * m:
        s = m - y
        return s


'''distance = where_should_i_swim_v5(10, 86, 3, 43)
print(distance)
assert distance == 3
'''

distance = where_should_i_swim_v5(49, 53, 17, 21)
print(distance)
