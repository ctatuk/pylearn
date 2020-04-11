'''
Для печати значений в Питоне есть функция print(). Внутри круглых скобок через запятую мы пишем то, что хотим вывести.
 Вот программа, которая делает несколько вычислений:
'''
'''
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # две звёздочки означают возведение в степень
print(37 / 3)  # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша считают частное от деления нацело
                # это как операция div в других языках
print(37 % 3)  # процент считает остаток от деления нацело
               # это как операция mod в других языках
'''

#print('Как вас зовут?')
#name = input()
#print('Hi' + name + '!')

'''
a = int(input())
b = int(input())
c = int(input())

print(a + b + c)'''


'''
a = int(input())
b = int(input())
s = 1/2 * a * b
print(s)'''


'''
print('n - число школьников')
print('k - количество яблок')
print('Введите n и k')
n = int(input())
k = int(input())
print('apples must be eat = ' + str(k//n))
print('apples stay in basket = ' + str(k%n))'''


'''
print('n - minutes')
print("m - hours")
n = int(input())
m = int(input())
print(str(n//60) + ':' + (n%60))'''

'''
print('ВВедите количество минут, прошедших с начала суток')
n = int(input())
number_of_hours = (n // 60) % 24
number_of_minutes = n % 60
print('Часы показывают: ' + str(number_of_hours) + ':' + str(number_of_minutes))
print('Часы показывают: %s:%s' % (number_of_hours, number_of_minutes))'''

'''
print('Введите ваше имя')
name = input()
print('"Hello, %s"'%name)
print('"Hello, {}"'.format(name))
print('"{}, {}"'.format("Hello", name))
print('"{b}, {a}"'.format(a="Hello", b=name))'''

'''
print('Введите число')
x = int(input())
# input всегда пустой, всегда строка!!!
m = x+1
y = x-1
print('The next number for the number ' + str(x) + ' is ' + str(m))
print('The previous number for the number ' + str(x) + ' is ' + str(y))

print('Введите число учеников в трёх классах для расчёта количества парт')
n = int(input())
m = int(input())
g = int(input())
x = n//2
y = m//2
z = g//2
if n%2>0:
    x = x+1
if m%2>0:
    y = y+1
if g%2>0:
    z = z+1
print('desks in class one ' + str(x))
print('desks in class two ' + str(y))
print('desks in class three ' + str(z))
print(x+y+z)

from math import ceil
print('Введите число учеников в трёх классах для расчёта количества парт')
n = float(input())
m = float(input())
g = float(input())
x = ceil(n/2)
y = ceil(m/2)
z = ceil(g/2)
print('desks in class one ' + str(x))
print('desks in class two ' + str(y))
print('desks in class three ' + str(z))
print(x+y+z)'''

import math
x=2.75
y=2.011
print(math.ceil(x))
print(math.ceil(y))


