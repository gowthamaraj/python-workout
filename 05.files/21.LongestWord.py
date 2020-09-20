'''
In this exercise, write two functions. find_longest_word takes a filename as an
argument and returns the longest word found in the file. The second function, find-
_all_longest_words, takes a directory name and returns a dict in which the keys are
filenames and the values are the longest words from each file.
'''

import os


def find_longest_word(filename: str)-> str:
    """
    fins the longest word in a file
    """
    longest_word = ''
    for line in open(filename,'r',encoding='utf-8'):
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word


def find_all_longest_words(dirname: str)-> dict:
    """
    TO find all the longest words in a dir containing many txt files
    """
    return {filename:find_longest_word(os.path.join(dirname,filename)) for filename in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,filename))}


print(find_all_longest_words('books'))