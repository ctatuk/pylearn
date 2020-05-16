def queenmove(queen_stay):
    queen_full = []
    print(len(queen_stay))
    print(queen_stay)
    for i, j in queen_stay:
            #print('this is', i, j)
            for x, y in range(len(queen_stay)):
                #print('what this', x, y)
                if i == x or j == y or abs(i-x) == abs(j-y):
                    print('ýes')
                else:
                    print('no')
        #queen_full.extend([i,j])
    #print(queen_full)


queenmove([(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)])
