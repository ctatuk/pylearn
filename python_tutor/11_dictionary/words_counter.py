'''
    Source: https://pythontutor.ru/lessons/dicts/problems/most_frequent_word/
    Condition
    The text is given: the first line contains the number of lines, then the lines themselves go.
    Print the word that is most often found in this text.
    If there are several such words, print the one that is less in lexicographical order.
    Дан текст: в первой строке задано число строк, далее идут сами строки.
    Выведите слово, которое в этом тексте встречается чаще всего.
    Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
'''
import re
from itertools import groupby


def create_dictionary(text):
    sep_list = re.split('[., ;\n]', text)
    dictionary = {}
    for i in sep_list:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary


def most_frequent_word(words):
    words_list = create_dictionary(words)
    print(words_list)
    max_value = max(words_list.values())
    max_key = {key for key, value in words_list.items() if value == max_value}
    print(max_key)
    key_dict = {}
    for i, j in enumerate(max_key):
        key_dict[i] = j, len(j)
    print(key_dict)
    print('_______________________')


def most_frequent_word2(words):
    word_counts = create_dictionary(words)
    # sorting by count descending, then len ascending
    sorted_counts = sorted(word_counts.items(), key=lambda item: (item[1], -len(item[0])), reverse=True)
    # get maximum frequency items only via groupby
    max_len, items = [(k, list(g)) for k, g in groupby(sorted_counts, lambda item: item[1])][0]
    print('most_frequent_word2', max_len, [item[0] for item in items])


def most_frequent_word3(words):
    word_counts = create_dictionary(words)
    # sorting by count descending, then len ascending
    sorted_counts = sorted(word_counts.items(), key=lambda item: (item[1], -len(item[0])), reverse=True)
    # get maximum frequency items only via list comprehension
    max_freq, items = sorted_counts[0][1], [item[0] for item in sorted_counts if item[1] == sorted_counts[0][1]]
    print('most_frequent_word3', max_freq, items)


most_frequent_word(
    '''zc gdwbsv uwsz j bqz cytzpsdpl q zczwrq e zvnisf cytzpsdpl gdwbsv cytzpsdpl e bqz bqz zczwrq gdwbsv gdwbsv e''')
most_frequent_word(
    '''zc gdwbsv bqz uwsz j bqz cytzpsdpl q zczwrq e zvnisf cytzpsdpl gdwbsv cytzpsdpl e bqz bqz zczwrq gdwbsv gdwbsv e''')
most_frequent_word(
    '''zc gdwbsv bqz uwsz j bqz cytzpsdpl a zczwrq e zvnisf e cytzpsdpl a a a q q q gdwbsv cytzpsdpl e bqz bqz zczwrq gdwbsv gdwbsv e''')
most_frequent_word2(
    '''zc gdwbsv bqz uwsz j bqz cytzpsdpl a zczwrq e zvnisf e cytzpsdpl a a a q q q gdwbsv cytzpsdpl e bqz bqz zczwrq gdwbsv gdwbsv e''')
most_frequent_word3(
    '''zc gdwbsv bqz uwsz j bqz cytzpsdpl a zczwrq e zvnisf e cytzpsdpl a a a q q q gdwbsv cytzpsdpl e bqz bqz zczwrq gdwbsv gdwbsv e''')
