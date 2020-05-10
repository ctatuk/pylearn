'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/factorial/
    Condition
    The factorial of n is the product 1 × 2 × ... × n. Designation: n !.
    For a given positive integer n, calculate the value of n !.
    Using the math math library in this task is prohibited.
'''
def factorial(num):
    fact = 1
    for i in range(1, num):
        fact = fact*i
        print(fact)
factorial(10)

'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/how_many_zeroes/
    Condition
    Given N numbers: first enter the number N, 
    then enter exactly N integers.
     Count the number of zeros among the entered numbers and print this number. 
    You need to count the number of numbers equal to zero,
    not the number of digits.
'''
def zero_counter(num_list):
    counter = 0
    num = len(num_list)
    indices = range(num)
    #print(indices)
    #print(list(indices))
    #zip_list = list(zip(num_list, indices))
    #print(zip_list)
    for i in zip(num_list, indices):
        if i[0] == 0:
            counter += 1
            print(i)
zero_counter([1, 0, 10, 30, 0, 7, 25, 0, 75])

'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/ladder/
    Condition
    Given a positive integer n ≤ 9, output a ladder from n steps,
    the i-th step consists of numbers from 1 to i without spaces.
'''
def stair(num):
    if num <= 9:
        s = ''
        for i in range(1, num):
            s = s + str(i)
            print(s)
stair(7)
