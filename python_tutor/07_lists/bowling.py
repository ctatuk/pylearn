def bowling(ninepins, thow_list):
    '''
    Source https://pythontutor.ru/lessons/lists/problems/kegelbahn/
    Condition
    N pins were put in one row, numbering them from left to right with numbers from 1 to N.
    Then K balls were thrown along this row, and the ith ball knocked down all the pins with numbers from li to ri
    inclusive. Determine which pins are left standing in place.
    The program receives at the input the number of pins N and the number of throws K.
    Next comes K pairs of numbers li, ri, with 1≤ li≤ ri≤ N.

    The program should output a sequence of N characters, where the jth character is “I” if the jth pin remains standing,
    or “.” If the jth pin was knocked down.
    '''
    counter = 0
    throw_result = []
    for i in range(1, ninepins + 1):
        throw_result.append(1)
    print('Bowling start:      ', throw_result)

    for start, end in thow_list:
        counter += 1
        if not 1 <= start <= end <= ninepins:
            print('Attempt: ', counter, 'Result: ', 'impossible throw')
        for elem in range(start - 1, end):
            throw_result[elem] = 0

        print('Attempt: ', counter, 'Result: ', throw_result)


bowling(15, [(2, 5), (8, 7), (10, 12)])
