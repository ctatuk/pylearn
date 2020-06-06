def rank_position(list_u, x):
    """
    Source https://pythontutor.ru/lessons/lists/problems/lineup/
    Condition
    Petya moved to another school. In a physical education lesson,
    he needed to determine his place in the ranks. Help him do this.
    The program receives a non-increasing sequence of natural numbers,
    which means the growth of each person in the system.
    After that, enter the number X - Petit's growth.
    All numbers in the input are natural and do not exceed 200.

    Print the number under which Petya should stand in line.
    If there are people in the ranks with the same height,
    the same as Petya, then he must get up after them.
    """
    list_u.sort()
    rank = []
    i = 0
    while list_u:
        if len(list_u) == i:
            break
        if list_u[i] < x < list_u[i + 1] or list_u[i] == x:
            rank.append(list_u[i])
            rank.append(x)
            position = len(rank)
        else:
            rank.append(list_u[i])
        i += 1
    print(rank, position)


rank_position([145, 150, 140, 142, 151, 139], 141)
