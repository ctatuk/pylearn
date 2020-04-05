'''
Для печати значений в Питоне есть функция print(). Внутри круглых скобок через запятую мы пишем то, что хотим вывести.
 Вот программа, которая делает несколько вычислений:

'''
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # две звёздочки означают возведение в степень
print(37 / 3)  # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша считают частное от деления нацело
                # это как операция div в других языках
print(37 % 3)  # процент считает остаток от деления нацело
               # это как операция mod в других языках

#print('Как вас зовут?')
#name = input()
#print('Hi' + name + '!')


'''a = int(input())
b = int(input())
c = int(input())

print(a + b + c)'''


'''a = int(input())
b = int(input())
s = 1/2 * a * b
print(s)'''


'''print('n - число школьников')
print('k - количество яблок')
print('Введите n и k')
n = int(input())
k = int(input())
print('apples must be eat = ' + str(k//n))
print('apples stay in basket = ' + str(k%n))'''


'''print('n - minutes')
print("m - hours")
n = int(input())
m = int(input())
print(str(n//60) + ':' + (n%60))'''

print('ВВедите количество минут, прошедших с начала суток')
n = int(input())
number_of_hours = (n // 60) % 24
number_of_minutes = n % 60
print('Часы показывают: ' + str(number_of_hours) + ':' + str(number_of_minutes))
print('Часы показывают: %s:%s' % (number_of_hours, number_of_minutes))

