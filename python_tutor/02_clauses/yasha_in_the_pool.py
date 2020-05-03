def where_should_i_swim_v1(M, N, x, y):
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/
    Condition
    Yasha swam in a N × M meter pool and was tired.
    At that moment, he discovered that he was at a distance of x meters
    from one of the long sides (not necessarily from the nearest) and y meters from one of the short sides.
    What is the minimum distance Yasha must swim to get out of the pool to the side?
    The program receives the input numbers N, M, x, y.
    The program should print the number of meters that you need to swim Yasha to the side.
    """
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
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/
    Condition
    Yasha swam in a N × M meter pool and was tired.
    At that moment, he discovered that he was at a distance of x meters
    from one of the long sides (not necessarily from the nearest) and y meters from one of the short sides.
    What is the minimum distance Yasha must swim to get out of the pool to the side?
    The program receives the input numbers N, M, x, y.
    The program should print the number of meters that you need to swim Yasha to the side.
    """
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
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/
    Condition
    Yasha swam in a N × M meter pool and was tired.
    At that moment, he discovered that he was at a distance of x meters
    from one of the long sides (not necessarily from the nearest) and y meters from one of the short sides.
    What is the minimum distance Yasha must swim to get out of the pool to the side?
    The program receives the input numbers N, M, x, y.
    The program should print the number of meters that you need to swim Yasha to the side.
    """
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
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/
    Condition
    Yasha swam in a N × M meter pool and was tired.
    At that moment, he discovered that he was at a distance of x meters
    from one of the long sides (not necessarily from the nearest) and y meters from one of the short sides.
    What is the minimum distance Yasha must swim to get out of the pool to the side?
    The program receives the input numbers N, M, x, y.
    The program should print the number of meters that you need to swim Yasha to the side.
    """
    if M < 0 or N < 0:
        print("Looks like this is not a pool. Puzzling...")
        return
    if x > M or x < 0 or y > N or y < 0:
        print("Looks like I'm already out! Hurray")
        return

    return min(x, y, M - x, N - y)


def where_should_i_swim_v5(n, m, x, y):
    """
    Source https://pythontutor.ru/lessons/ifelse/problems/jacob_the_swimmer/
    Condition
    Yasha swam in a N × M meter pool and was tired.
    At that moment, he discovered that he was at a distance of x meters
    from one of the long sides (not necessarily from the nearest) and y meters from one of the short sides.
    What is the minimum distance Yasha must swim to get out of the pool to the side?
    The program receives the input numbers N, M, x, y.
    The program should print the number of meters that you need to swim Yasha to the side.
    """
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


distance = where_should_i_swim_v1(49, 53, 17, 21)
print(distance)

distance = where_should_i_swim_v2(49, 53, 17, 21)
print(distance)

distance = where_should_i_swim_v3(49, 53, 17, 21)
print(distance)

distance = where_should_i_swim_v4(49, 53, 17, 21)
print(distance)

distance = where_should_i_swim_v5(49, 53, 17, 21)
print(distance)
