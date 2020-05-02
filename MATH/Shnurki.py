'''Обувная фабрика собирается начать выпуск элитной модели ботинок. Дырочки для шнуровки будут расположены в два ряда,
расстояние между рядами равно a, а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N.
Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх, по горизонтали и т.д.” (см.
рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком, длина свободного конца шнурка должна быть l

. Какова должна быть длина шнурка для этих ботинок?

Программа получает на вход четыре натуральных числа a
, b, l и N - именно в таком порядке - и должна вывести одно число - искомую длину шнурка.'''


def shoe_laces(a, b, l, n):
    length = (a + b) * 2 * n + l - a
    print(length)


# shoe_laces(2, 1, 3, 4)

'''Задача «Знак числа»
Условие
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.

Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if...
elif... else. '''


def sign_x(x):
    if x > 0:
        print('1')
    elif x < 0:
        print('-1')
    else:
        print('0')


sign_x(0)

'''Задача «Шахматная доска»
Условие
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой
клетки, потом для второй клетки. '''


def chess(x1, y1, x2, y2):
    if (x1 + y1) % 2 == 0:
        cell1 = True
    else:
        cell1 = False
    if (x2 + y2) % 2 == 0:
        cell2 = True
    else:
        cell2 = False
    if cell1 == cell2:
        print('Клетки одного цвета')
    else:
        print('Клетки разного цвета')


# chess(1, 1, 2, 6)


def cell(x, y):
    if (x + y) % 2 == 0:
        return True
    else:
        return False


def chess2(x1, y1, x2, y2):
    cell1 = cell(x1, y1)
    cell2 = cell(x2, y2)
    if cell1 == cell2:
        print('Клетки одного цвета')
    else:
        print('Клетки разного цвета')


# chess2(1, 1, 2, 6)

'''Задача «Високосный год»
Условие
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным,
то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400. '''


def what_year(x):
    if x % 4 == 0 or x % 400 == 0 and not x % 100 == 0:
        print('год високосный')
    else:
        print('год не високосный')


# what_year(2019)


'''Задача «Минимум из трех чисел»
Условие
Даны три целых числа. Выведите значение наименьшего из них.'''


def min_three(a, b, c):
    if a < b and a < c:
        print('a')
    elif b < c:
        print('b')
    else:
        print('c')


# min_three(1, 2, 3)
# min_three(2, 1, 3)
# min_three(3, 2, 1)


'''Задача «Сколько совпадает чисел»
Условие
Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все
совпадают), 2 (если два совпадает) или 0 (если все числа различны). '''


def equality(a, b, c):
    if a == b and b == c and a == c:
        print('3')
    elif a == b or b == c or a == c:
        print('2')
    else:
        print('0')


# equality(3, 3, 3)
# equality(1, 2, 3)
# equality(2, 3, 2)


'''Задача «Ход ладьи»
Условие
Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли
ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие
номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, если из
первой клетки ходом ладьи можно попасть во вторую или NO в противном случае. '''


def rook(x1, y1, x2, y2):
    for elem in x1, y1, x2, y2:
        print(elem)
        if elem not in range(1, 9):
            print('use numbers from 1 to 8')
            break
    if x1 == x2 or y1 == y2:
        print('yes')
    else:
        print('no')


# rook(4, 4, 4, 8)
# rook(5, 1, 4, 6)
# rook(0, 1, 8, 3)

'''Условие
Задача «Ход короля»
Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны две различные клетки шахматной
доски, определите, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре
числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.'''


def king(x1, y1, x2, y2):
    for elem in x1, y1, x2, y2:
        print(elem)
        if elem not in range(1, 9):
            print('use numbers from 1 to 8')
            break
    if x2 == x1 + 1 or x2 == x1 - 1 or y2 == y1 + 1 or y2 == y1 - 1:
        print('yes')
    else:
        print('no')


# king(3, 3, 4, 4)
# king(1, 1, 1, 3)


'''Задача «Ход слона»
Условие
Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой
клетки на вторую одним ходом. '''


def elephant(x1, y1, x2, y2):
    for elem in x1, y1, x2, y2:
        print(elem)
        if elem not in range(1, 9):
            print('use numbers from 1 to 8')
            break
    if abs(x1-x2) == abs(y1-y2):
        print('yes')
    else:
        print('no')

#elephant(3, 3, 4, 5)
#elephant(3, 4, 2, 4)
#elephant(6, 6, 7, 5)

'''a,c,b,d = (int(input()) for _ in range(4))
print('YES' if abs(a - b) == abs(c - d) else 'NO')'''


'''Задача «Ход ферзя»
Условие

Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки шахматной доски, определите,
может ли ферзь попасть с первой клетки на вторую одним ходом. '''

def queen(x1, y1, x2, y2):
    for elem in x1, y1, x2, y2:
        print(elem)
        if elem not in range(1, 9):
            print('use numbers from 1 to 8')
            break
    if abs(x1-x2) == abs(y1-y2):
        print('yes')
    elif x1 == x2 or y1 == y2:
        print('yes')
    else:
        print('no')

#queen(1, 1, 2, 2)
#queen(1, 1, 2, 3)
#queen(6, 5, 2, 5)

'''
Задача «Ход коня»
Условие

Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или
наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним
ходом.
'''


def horse(x1, y1, x2, y2)