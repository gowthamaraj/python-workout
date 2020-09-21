"""
 In this exercise, we’re going to create a password-generation function. Actually,
we’re going to create a factory for password-generation functions. That is, I might
need to generate a large number of passwords, all of which use the same set of characters. (You know how it is. Some applications require a mix of capital letters, lowercase
letters, numbers, and symbols; whereas others require that you only use letters; and
still others allow both letters and digits.) You’ll thus call the function create_password
_generator with a string. That string will return a function, which itself takes an integer
argument. Calling this function will return a password of the specified length, using
the string from which it was created;
"""


import random

def create_password_generator(word: str):
    def return_pwd(length: int):
        return ''.join([random.choice(word) for i in range(length)])
    return return_pwd

    
alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')
print(alpha_password(5))
print(alpha_password(10))
print(symbol_password(5))
print(symbol_password(10))
