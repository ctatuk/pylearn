'''
Даны два целых числа A и В. Выведите все числа от A до B включительно,
в порядке возрастания, если A < B,или в порядке убывания в противном случае.
'''
def ranks_two(a, b):
    if a < b:
        for i in range(a, b + 1):
            i <= 1
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)
ranks_two(-3, -7)