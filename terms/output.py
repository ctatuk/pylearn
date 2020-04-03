#1 Задача "Сумма трех чисел"

#a = int(input())
#b = int(input())
#c = int(input())
#print(a + b + c)

#2 Задача "Площадь прямоугольного треугольника

#h = int(input())
#b = int(input())
#s = 1/2 * b * h
#print(s)

#3 задача ход ферзя

def compare_chess_queen(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        print('Yes')
    elif abs(x2 - x1) == abs(y2 - y1):
        print('Yes')
    else:
        print('No')
compare_chess_queen(7, 5, 1, 1)


