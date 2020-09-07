'''
 This challenge asks you to redefine the mysum function we defined in chapter 1,
such that it can take any number of arguments. The arguments must all be of the
same type and know how to respond to the + operator. (Thus, the function should
work with numbers, strings, lists, and tuples, but not with sets and dicts.)

The result should be a new, longer sequence of the type provided by the parameters.
Thus, the result of mysum('abc', 'def') will be the string abcdef, and the result of
mysum([1,2,3], [4,5,6]) will be the six-element list [1,2,3,4,5,6]. Of course, it
should also still return the integer 6 if we invoke mysum(1,2,3).
'''


def mysum(*items):
    '''
    to sum the input
    '''
    if not items: return ()
    output = items[0]
    for i in items[1:]:
        output += i
    return output


print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))