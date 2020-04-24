from typing import Any, Tuple, Union


def cycle_while(a):
    n = 0
    while a[n] != 0:
        if a[n] == ' ':
            print('Встретилось отрицательное число', a[:n])
            print(a[n - 1])
            break
        n += 1
    else:
        print('Ни одного отрицательного числа не встретилось')


# cycle_while('asdf sdflkj')

def cycle_for(a):
    for i in range(0, len(a)):
        if a[i] == ' ':
            print('Встретилось отрицательное число', a[:i])
            break
        else:
            print('Ни одного отрицательного числа не встретилось')


# cycle_for('asdf sdflkj')

'''
В первый день спортсмен пробежал x километров, 
а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
По данному числу y определите номер дня, 
на который пробег спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y
 и должна вывести одно натуральное число. 
'''


def run_morning(x, y):  # х километров в первый день, y км пробежал всего
    days = 1
    while x < y:
        x = x + x * 0.1
        days += 1
    print(days)


# run_morning(10, 20)

'''
Определите сумму всех элементов последовательности,
 завершающейся числом 0. В этой и во всех следующих задачах числа,
 следующие за первым нулем, учитывать не нужно. 
'''


def summa_chain(s):
    n = 0
    while s[n] > 0:
        n += 1
    print(sum(s))


# summa_chain([1, 5, 8, 32, 876, 0])

'''
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
По данному числу n определите n-е число Фибоначчи φn.
Эту задачу можно решать и циклом for
'''


def fibonachi(k):
    if k < 1:
        print('0')
        return 0
    elif k == 1:
        print('1')
        return 1
    else:

        return fibonachi(k - 2) + fibonachi(k - 1)


# result = fibonachi(4)
# print(result)

def fibonacci(n):
    fn = f0 = 0
    f1 = 1
    i = 0
    if n == 1:
        print(1)
    elif n == 0:
        print(0)
    else:
        while i + 1 < n:
            fn = f1 + f0
            f0, f1 = f1, fn
            i += 1
        print(fn)


# fibonacci(6)

def fib():
    fibonacci = [0, 1]
    i = 1
    while fibonacci[-1] < 18:
        print(fibonacci[-1])
        i += 1
        print(fibonacci[i - 2], fibonacci[i - 1])
        new_term = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(new_term)


#   print(fibonacci)
# fib()

'''
Дано натуральное число A. Определите,
 каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φn = A. 
Если А не является числом Фибоначчи, выведите число -1. 
'''


def fibonacci_num(A):
    fibonacci = [0, 1]
    i = 1
    while fibonacci[-1] < A:
        i += 1
        print(fibonacci[i - 2] + fibonacci[i - 1])
        new_term = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(new_term)
        if new_term > A or A < 1:
            print(-1)
            break
        elif new_term == A:
            print(i)
            break


fibonacci_num(1134903170)
