import re


def number_of_words(words):
    b = re.split('[., ;\n]', words)
    for i in b:
        if i == '' or i == '\n':
            b.remove(i)
    print(b)
    result = len(set(b))
    print(result)


def number_of_words2(text):
    a = [x for x in re.split('[., ;\n]', text) if x != '']
    print(a)
    print(len(set(a)))


number_of_words('''She sells sea shells on the sea shore; 
The shells that she sells are sea shells I'
m sure. So if she sells sea shells on the sea shore, 
I'm sure that the shells are sea shore shells.''')

number_of_words2('''She sells sea shells on the sea shore; 
The shells that she sells are sea shells I'
m sure. So if she sells sea shells on the sea shore, 
I'm sure that the shells are sea shore shells.''')