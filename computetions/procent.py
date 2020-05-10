'''
    Source: http://pythontutor.ru/lessons/int_and_float/problems/percents/
    Condition
    The interest rate on the deposit is P percent per annum,
    which are added to the deposit amount. The contribution is X rubles Y kopecks.
    Determine the size of the contribution in a year.
    The program receives integers P, X, Y and
    contribution value in a year in rubles and kopecks.
    The fractional part of kopecks is discarded.
'''
from math import ceil
def size_deposit(percent, amount_rub, amount_cents):
    summ = amount_rub + 0.01 * amount_cents
    deposit = summ / 100 * percent + summ
    result = ceil(deposit * 100)
    return result // 100, result % 100
print(size_deposit(10, 100, 25))

