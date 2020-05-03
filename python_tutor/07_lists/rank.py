def rank_position(list_u, x):
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
