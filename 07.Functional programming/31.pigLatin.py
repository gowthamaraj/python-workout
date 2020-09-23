"""
 In this exercise, I want you to write a function that takes a filename as an argument. It returns a string with the file’s contents, but with each word translated into Pig
Latin, as per our plword function in chapter 2 on “strings.” The returned translation
can ignore newlines and isn’t required to handle capitalization and punctuation in
any specific way.
"""

def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    return word[1:] + word[0] + 'ay'

def plfile(filename):
    return ' '.join([ plword(word) for line in open(filename) for word in line.split()])

print(plfile('input.txt'))