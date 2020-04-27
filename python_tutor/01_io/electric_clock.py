
def electronic_clock(m):
    """
    Source https://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/electronic_watch/
    Condition
    Given the number n. Since the beginning of the day n minutes have passed.
    Determine how many hours and minutes the electronic clock will show at this moment.
    The program should print two numbers: the number of hours (from 0 to 23)
    and the number of minutes (from 0 to 59).
    Note that the number n may be greater than the number of minutes in a day.
    """
    print(str(m // 60) + ':' + str(n % 60))
