'''
    Source: http://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/electronic_watch/
    Condition
    Given the number n. Since the beginning of the day n minutes have passed.
     Determine how many hours and minutes the electronic clock
     will show at this moment.
    The program should print two numbers:
    the number of hours (from 0 to 23) and the number of minutes (from 0 to 59).
    Note that the number n may be greater than the number of minutes in a day.
'''
print('n - minute')
n = int(input())
number_of_hours = n // 60 % 24
number_of_min = n % 60
print(str(number_of_hours) + ':' + str(number_of_min))


