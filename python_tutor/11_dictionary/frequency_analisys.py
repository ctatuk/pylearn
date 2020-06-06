'''
    Source: https://pythontutor.ru/lessons/dicts/problems/frequency_analysis/
    Condition
    Given text: the first line contains the number of lines in the text,
    and then the lines themselves. Print all the words that appear in the text,
    one for each line. Words should be sorted in descending order of the number of occurrences in the text,
    and at the same frequency of occurrence - in lexicographical order.

    Indication After you create a dictionary of all words, you will want to sort
    it by the frequency of occurrence of the word. You can achieve what you want by creating
    a list whose elements are tuples of two elements: the frequency of occurrence of the word
    and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then standard sorting will
    sort the list of tuples, while the tuples are compared by the first element,
    and if they are equal, then by the second. This is almost what is required in the task.
'''
import re
def create_dictionary(text):
        word_list = [x for x in re.split('[., ;\n]', text) if x != '']
        from collections import defaultdict
        dictionary = defaultdict(int)
        for word in word_list:
            dictionary[word] += 1
        return dict(dictionary)

def frequency_analysis(text):
    dictionary = create_dictionary(text)
    inversed_word_list = [(v, k) for (k, v) in dictionary.items()]
    print(inversed_word_list)
    sort_word_list = sorted(inversed_word_list, key= lambda item: item[1])
    print(sort_word_list)
    sorted_counts = sorted(sort_word_list, key=lambda item: item[0], reverse=True)
    print(sorted_counts)


frequency_analysis("""
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
""")