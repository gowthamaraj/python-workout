'''
For this exercise, 
you need to write a function (hex_output) that takes a hex number and returns the decimal equivalent.

That is, if the user enters 50, you’ll assume
that it’s a hex number (equal to 0x50) and will print the value 80 to the screen. 
And
no, you shouldn’t convert the number all at once using the int function, although it’s
permissible to use int one digit at a time.
'''

def hex_output():
    '''
    A function that takes a hex number and returns the decimal equivalent.
    '''

    dec_num = 0
    hex_num = input('Enter a hex number to convert:  ')
    for position, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** position)
    print(dec_num) 

hex_output()