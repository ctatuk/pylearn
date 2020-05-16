def unic_element(list_elem):
    for i in range(len(list_elem)):
        for j in range(len(list_elem)):
            if i!=j and list_elem[i] == list_elem[j]:
                break
        else:
            print(list_elem[i], end='')


unic_element([1,2,2,3,4,4,5])