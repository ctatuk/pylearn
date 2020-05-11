def swap_minmax(unique_list):
    '''
    Source https://pythontutor.ru/lessons/lists/problems/swap_min_and_max/
    Condition
    In the list, all elements are different. Swap the minimum and maximum element of this list.
    '''
    sorted_list = sorted(unique_list)
    min_elem = sorted_list[0]
    max_elem = sorted_list[-1]
    min_index = unique_list.index(min_elem)
    max_index = unique_list.index(max_elem)
    unique_list[min_index] = max_elem
    unique_list[max_index] = min_elem
    print(unique_list)


def swap_minmax2(unique_list):
    '''
    Source https://pythontutor.ru/lessons/lists/problems/swap_min_and_max/
    Condition
    In the list, all elements are different. Swap the minimum and maximum element of this list.
    '''
    min_elem = unique_list[0]
    max_elem = unique_list[0]
    min_index = 0
    max_index = 0
    for index, elem in enumerate(unique_list):
        if elem < min_elem:
            min_elem, min_index = elem, index
        if elem > max_elem:
            max_elem, max_index = elem, index
    unique_list[min_index] = max_elem
    unique_list[max_index] = min_elem
    print(unique_list)


swap_minmax2([1, 3, 5, 6, 2, 0])
swap_minmax([1, 3, 5, 6, 2, 0])
