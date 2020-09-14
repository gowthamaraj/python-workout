'''
 The challenge for this exercise is to write a wordcount function that mimics the wc
Unix command. The function will take a filename as input and will print four lines
of output:
1 Number of characters (including whitespace)
2 Number of words (separated by whitespace)
3 Number of lines
4 Number of unique words (case sensitive, so “NO” is different from “no”)
'''


def wordcount(filename):
    counts = {'char': 0, 'words': 0, 'lines': 0}
    unique_words = set()

    with open(filename) as file:
        for line in file:
            counts['lines'] += 1
            counts['char'] += len(line)
            counts['words'] += len(line.split())
            unique_words.update(line.split())
    counts['unique_words'] = len(unique_words)

    for k,v in counts.items():
        print(f'{k} - {v}')

wordcount('05.files\count.txt')