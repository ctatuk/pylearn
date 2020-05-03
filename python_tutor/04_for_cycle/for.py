def rainbow():
    """
    Source https://pythontutor.ru/lessons/for_loop/
    :return: rainbow
    """
    i = 1
    for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
        print('#', i, ' color of rainbow is ', color, sep='')
        i += 1


def factorial(num):
    """
    Source https://pythontutor.ru/lessons/for_loop/problems/factorial/
    Condition
    The factorial of n is the product 1 × 2 × ... × n. Designation: n !.
    For a given positive integer n, calculate the value of n !. Using the math math library in this task is prohibited.
    """
    fact = 1
    for i in range(1, num):
        fact = fact * i
        print(fact)


factorial(10)


def zero_counter(num_list):
    """
    Source https://pythontutor.ru/lessons/for_loop/problems/how_many_zeroes/
    Condition
    Given N numbers: first enter the number N, then enter exactly N integers.
    Count the number of zeros among the numbers entered and print this number.
    You need to count the number of numbers equal to zero, not the number of digits.
    """
    counter = 0
    num = len(num_list)
    indices = range(num)

    for i in zip(num_list, indices):
        if i[0] == 0:
            counter += 1
            print(i)


zero_counter([1, 0, 10, 30, 0, 7, 25, 0, 75])
