'''
    Source: http://pythontutor.ru/lessons/str/problems/two_halves/
    Condition
    Given a string. Cut it into two equal parts (if the line length is even,
    and if the line length is odd, then the length of the first
    parts should be one character more). Rearrange these two parts,
    write the result in a new line and display.
'''
from math import ceil
def half_string(s):
    n = int(ceil(len(s)/2))
    print(len(s))
    print(s[n:], s[:n])
half_string('white rabbit jump')
