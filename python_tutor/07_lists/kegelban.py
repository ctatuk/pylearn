def bowling(ninepins, thow_list):
    counter = 0
    throw_result = []
    for i in range(1, ninepins + 1):
        throw_result.append(1)
    print('Bowling start:      ', throw_result)

    for start, end in thow_list:
        counter += 1
        if not 1<=start<=end<=ninepins:
            print('Attempt: ', counter, 'Result: ', 'impossible throw')
        for elem in range(start - 1, end):
            throw_result[elem] = 0

        print('Attempt: ', counter, 'Result: ', throw_result)


bowling(15, [(2, 5), (8, 7), (10, 12)])