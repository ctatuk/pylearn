#1 Задача "Сумма трех чисел"

#a = int(input())
#b = int(input())
#c = int(input())
#print(a + b + c)

#2 Задача "Площадь прямоугольного треугольника

#h = int(input())
'''b = int(input())
s = 1/2 * b * h
print(s)'''

#3 задача ход ферзя

'''def compare_chess_queen(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        print('Yes')
    elif abs(x2 - x1) == abs(y2 - y1):
        print('Yes')
    else:
        print('No')
compare_chess_queen(7, 5, 1, 1)'''

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
    if x < m and y < n:
        print('Yasha in the pool')
    if x > m or y > n:
        print('Yasha out of pool')
    a = m - x
    b = n - y
    if x <= a and x < y:
        print(x)
    elif x >= a and a < b:
        print(a)
    elif y <= b and y < x:
        print(y)
    elif y >= b and b < a:
        print(b)

tired_in_pool(5, 94, 1, 36)




