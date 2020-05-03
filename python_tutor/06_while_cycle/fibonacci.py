def fibonacci(k):
    """
    Source https://pythontutor.ru/lessons/while/problems/kth_fibonacci/
    Condition
    The Fibonacci sequence is defined as follows:
    φ0 = 0, φ1 = 1, φn = φn − 1 + φn − 2.
    Given a number n, determine the nth Fibonacci number φn.
    This problem can also be solved with the for loop.
    """
    if k < 1:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


result = fibonacci(6)
print(result)
