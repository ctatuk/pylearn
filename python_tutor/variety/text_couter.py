'''

Условие
Дан текст: в первой строке записано число строк, далее идут сами строки.
 Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
'''

import re


def text_counter(text):
    c = re.split('[.;,\n ]', text)
    print(c)
    b = list(filter(None, c))
    print(b)

    print(len(b))
    print(len(set(b)))


def text_counter2(text):
    a = [x for x in re.split('[.;,\n ]', text) if x != '']
    print(len(set(a)))


text_counter2("""She sells sea shells on the sea shore;
                The shells that she sells are sea shells I'm sure.
                So if she sells sea shells on the sea shore,
                I'm sure that the shells are sea shore shells.""")
text_counter('a b a c a b a d a b a c a b a')
text_counter("""The other two, slight air, and purging fire,
Are both with thee, wherever I abide,
The first my thought, the other my desire,
These present-absent with swift motion slide.
For when these quicker elements are gone
In tender embassy of love to thee,
My life being made of four, with two alone,
Sinks down to death, oppressed with melancholy.
Until life's composition be recured,
By those swift messengers returned from thee,
Who even but now come back again assured,
Of thy fair health, recounting it to me.
This told, I joy, but then no longer glad,
I send them back again and straight grow sad.""")
