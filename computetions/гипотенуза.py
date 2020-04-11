"""Условие

Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
"""
import math
def find_hypotenuse(katet_a, katet_b):
    hypo_c = math.sqrt(katet_a ** 2 + katet_b ** 2)
    print(hypo_c)
find_hypotenuse(1, 1)
