def find_second_f(array, pattern):
    """
    Source https://pythontutor.ru/lessons/str/problems/second_occurence/
    Condition
    Given a string. Find in this line the second occurrence of the letter f,
    and print the index of this occurrence.
    If the letter f appears in this line only once, print the number -1,
    and if it does not occur even once, print the number -2.
    """

    if array.count(pattern) == 0:
        print(-2)
    elif array.count(pattern) == 1:
        print(-1)
    else:
        y = array.find(pattern, array.find(pattern) + 1)
        print(y, array[y])


find_second_f('aldsfkaofdaiur', 'f')
