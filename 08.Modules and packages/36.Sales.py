"""
In this exercise, you’ll implement a somewhat complex (and whimsical) function,
in a module, to implement tax policy in the Republic of Freedonia. The idea is that
the tax system is so complex that the government will supply businesses with a Python
module implementing the calculations for them.

 Moreover, I want you to write this solution using two separate files. The calculate
_tax function, as well as any supporting data and functions, should reside in the file
freedonia.py, a Python module. The program that calls calculate_tax should be in
a file called use_freedonia.py, which then uses import to load the function.
"""
from freedonia import calculate_tax

print(calculate_tax(500, 'Harpo', 12))