'''
Write a function,
1. it takes any number of arguments as input
2. return the sum of these numbers

Constraints,
1. do not use in-build sum() function
'''

from functools import reduce


def mysum(*number) -> int:
    return reduce(lambda x,y:x+y, number)


print(mysum(1,2,3,4))
# print((lambda *n:reduce(lambda x, y: x + y, n))(1,2))