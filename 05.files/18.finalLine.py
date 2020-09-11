'''
 In this exercise, write a function (get_final_line) that takes a filename as an
argument. The function should return that file’s final line on the screen.
'''

from io import StringIO

fakefile = StringIO('''
line 1
line 2
line 3
''')


def get_final_line(filename):
    output = ''
    for lines in fakefile:
        output = lines
    return output

print(get_final_line(fakefile), end='')
