"""
 For this exercise, I want you to write a function (calc) that expects a single
argument—a string containing a simple math expression in prefix notation—with an
operator and two numbers. Your program will parse the input and produce the appropriate output. For our purposes, it’s enough to handle the six basic arithmetic operations in Python: addition, subtraction, multiplication, division (/), modulus (%), and
exponentiation (**). The normal Python math rules should work, such that division
always results in a floating-point number. We’ll assume, for our purposes, that the
argument will only contain one of our six operators and two valid numbers
"""

import operator

def calc(to_solve):
    operations = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv,
        '**':operator.pow,
        '%':operator.mod
    }
    op, f, s = to_solve.split()
    return operations[op](int(f), int(s))

print(calc('+ 2 3'))