'''
For this exercise, write a Python function, format_sort_records, that takes the
PEOPLE list and returns a formatted string that looks like the following:

Trump   Donald     7.85
Putin   Vladimir   3.63
Xi      Jinping   10.60
'''

import operator
PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]

for item in sorted(PEOPLE, key= operator.itemgetter(1,0)):
    print(f'{item[1]:10}{item[0]:10}{item[2]:5.2f}')