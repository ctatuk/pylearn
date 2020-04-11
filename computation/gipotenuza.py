'''Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.'''

'''import math
a=int(input())
b=int(input())
c=math.sqrt(a**2+b**2)
print(c)'''

import math


def storony_triangle(katet1, katet2):
    if katet1 <= 0 or katet2 <= 0:
        print('Such triangle is unreal')
        return

    hypotenuse = math.sqrt(katet1 ** 2 + katet2 ** 2)
    print(hypotenuse)
storony_triangle(26, 89)
