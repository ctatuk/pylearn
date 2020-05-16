def list_two(b):
    '''
    source https://pythontutor.ru/lessons/lists/problems/even_elements/
    Condition
    Print all the even elements of the list. In doing so,
    use a for loop that iterates over the list items, not their indexes!

    '''
    for i in range(len(b)):
        if b[i]%2 == 0:
            print(b[i])


list_two([4, 5, 8, 9, 7, 6])