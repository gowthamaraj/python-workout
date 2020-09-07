'''
Write a function, firstlast, that takes
a sequence (string, list, or tuple) and returns the first and last elements of that
sequence, in a two-element sequence of the same type. So firstlast('abc') will
return the string ac, while firstlast([1,2,3,4]) will return the list [1,4].
'''

def firstlast(items):
    '''
    return 1st and last element 0 same dtype as input
    '''
    return items[:1] + items[-1:]


print(firstlast('abcd'))
print(firstlast([1,2,3,4]))
