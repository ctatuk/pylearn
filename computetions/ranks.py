# Ряды - 1
'''
Даны два целых числа A и B (при этом A ≤ B).
Выведите все числа от A до B включительно.
'''
def rank_one(a, b):
    a <= b
    for i in range(a, b + 1):
        i <= 1
        print(i)
rank_one(-3, 14)
