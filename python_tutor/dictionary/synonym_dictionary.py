'''
    Source: http://pythontutor.ru/lessons/dicts/problems/synonym_dictionary/
    Condition
    You are given a dictionary consisting of pairs of words.
    Each word is synonymous with a pair of words. All words in the dictionary are different.
    For a word from a dictionary written on the last line, define its synonym.
'''
def synonym_dictionary(dic, m):

    print(dic.values())
    print(dic.keys())
    a = [i for (i, j) in dic.items() if j == m]
    print(a)

synonym_dictionary({'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}, 'Goodbye')
