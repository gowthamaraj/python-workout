"""
In this exercise, we’ll practice doing such unraveling. Write a function that takes a
list of lists (just one element deep) and returns a flat, one-dimensional version of the
list. Thus, invoking
flatten([[1,2], [3,4]])
will return
[1,2,3,4]
"""


def flatten(data):
    return [ point for item in data for point in item]

print(flatten([[1,2], [3,4]]))