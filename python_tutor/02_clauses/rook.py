def rook(x1, y1, x2, y2):
    for elem in x1, y1, x2, y2:
        print(elem)
        if elem < 1 or elem > 8:
            print('use numbers from 1 to 8')
            break


rook(0, 3, 4, 5)
