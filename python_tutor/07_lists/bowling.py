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


def bowling_throws1(n, throws):
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
    pins = list(range(1, n + 1))
    print('pins = ' + str(pins))
    throws_expanded = []
    for throw_start, throw_end in throws:
        this_throw = list(range(throw_start, throw_end + 1))
        print(this_throw)
        throws_expanded.extend(this_throw)
    print('removed_pins = ' + str(throws_expanded))
    pins_result = []
    for pin in pins:
        pins_result.append(0 if pin in throws_expanded else 1)
    print(pins_result)


def bowling_throws2(n, throws):
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
    pins = list(range(1, n + 1))
    print('pins = ' + str(pins))
    throws_expanded = []
    for throw_start, throw_end in throws:
        this_throw = list(range(throw_start, throw_end + 1))
        print(this_throw)
        throws_expanded.extend(this_throw)
    print('removed_pins = ' + str(throws_expanded))
    pins_result = [0 if pin in throws_expanded else 1 for pin in pins]
    print(pins_result)


def bowling_throws3(n, throws):
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
    print(throws)
    pins = list(range(1, n + 1))
    print('pins = ' + str(pins))
    throws_expanded_p1 = [list(range(throw[0], throw[1] + 1)) for throw in throws]
    print('intermediate list = ' + str(throws_expanded_p1))
    throws_expanded_p2 = []
    for sublist in throws_expanded_p1:
        throws_expanded_p2 += sublist
    print('removed_pins = ' + str(throws_expanded_p2))
    pins_result = [0 if pin in throws_expanded_p2 else 1 for pin in pins]
    print(pins_result)


def bowling_throws4(n, throws):
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
    print(throws)
    pins = list(range(1, n + 1))
    print('pins = ' + str(pins))
    throws_expanded_p1 = [list(range(throw[0], throw[1] + 1)) for throw in throws]
    print('intermediate list = ' + str(throws_expanded_p1))
    from functools import reduce
    throws_expanded_p2 = reduce(lambda a, b: a + b, throws_expanded_p1)
    print('removed_pins = ' + str(throws_expanded_p2))
    pins_result = [0 if pin in throws_expanded_p2 else 1 for pin in pins]
    print(pins_result)


def bowling_throws5(n, throws):
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
    from functools import reduce
    throws_expanded = reduce(lambda a, b: a + b, [list(range(throw[0], throw[1] + 1)) for throw in throws])
    print([0 if pin in throws_expanded else 1 for pin in list(range(1, n + 1))])


bowling_throws5(12, [(1, 3), (4, 5), (7, 10)])
bowling(15, [(2, 5), (8, 7), (10, 12)])
