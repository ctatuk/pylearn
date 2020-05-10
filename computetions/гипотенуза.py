"""
    Source: http://pythontutor.ru/lessons/int_and_float/problems/hypo
    Condition
    Two numbers a and b are given. Derive the hypotenuse of a triangle with given legs.
"""
import math
def find_hypotenuse(katet_a, katet_b):
    hypo_c = math.sqrt(katet_a ** 2 + katet_b ** 2)
    print(hypo_c)
find_hypotenuse(1, 1)

import math
def find_hypotenuse(katet_a, katet_b):
    return math.hypot(katet_a, katet_b)
print(find_hypotenuse(3, 4))
