"""
In this exercise, we’re given a string, which we assume contains integers separated by
spaces. We want to grab the individual integers from the string and then sum them
together. The easiest way to do this is to invoke str.split on the string, which returns
a list of strings. By invoking str.split without any parameters, we tell Python that any
combination of whitespace should be used as a delimiter.
"""

def sum_numbers(word: str)-> int:
    data = word.split()
    return sum([int(i) for i in word if i.isdigit()])


print(sum_numbers('1 2 3 a b c 4'))