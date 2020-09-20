'''
 For this exercise, create a function, passwd_to_csv, that takes two filenames as
arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
'''

import csv
import os


def passwd_to_csv(p_filename, c_filename):

    with open(p_filename) as input, open(c_filename, 'w') as output:
        infile = csv.reader(input, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')

        for line in infile:
            if len(line) > 1:
                outfile.writerow((line[0], line[2]))


passwd_to_csv('passwd.txt', os.path.join('tmp','output.csv'))