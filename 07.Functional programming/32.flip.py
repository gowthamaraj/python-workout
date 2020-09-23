"""
 For this exercise, first create a dict of any size, in which the keys are unique and the
values are also unique. (A key may appear as a value, or vice versa.) Here’s an example:
d = {'a':1, 'b':2, 'c':3}
"""

def flipped_dict(data):
    return {v:k for k,v in data.items()}

print(flipped_dict({'a':1, 'b':2, 'c':3}))