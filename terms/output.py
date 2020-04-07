#1 Задача "Сумма трех чисел"

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#2 Задача "Площадь прямоугольного треугольника

h = int(input())
b = int(input())
s = 1/2 * b * h
print(s)

#3 задача ход ферзя

def compare_chess_queen(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        print('Yes')
    elif abs(x2 - x1) == abs(y2 - y1):
        print('Yes')
    else:
        print('No')
compare_chess_queen(7, 5, 1, 1)

# задача ход коня
#def compare_chess_horse(x1, y1, x2, y2):
   # if abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
   #     print('Yes')
   # elif abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
 #       print('Yes')
  #  else:
#        print('No')
#compare_chess_horse(2, 8, 3, 7)

#задача шоколадка
#def slices_of_chocolate(n, m, k):
 #   if (k % n == 0 or k % m == 0) and k < m * n:
#        print('Yes')
#    else:
#        print('No')
#slices_of_chocolate(1, 1, 2)

#задача Яша
def tired_in_pool(m, n, x, y):
    if abs(x1 - x) <= x and abs(y - y1) <= y1:
      m == x1 - x
    elif y - y1 <= y and x - x1 <= x1:
       n == y1 - y
    elif x < x1 and y < y1:
       print(x)
    elif y < y1 and x < x1:
     print(y)

tired_in_pool(5, 87, 3, 38)




