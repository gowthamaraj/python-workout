def reverse_line(inputFile, outputfile):
    with open(inputFile) as input, open(outputfile, 'w') as output:
        for line in input:
            output.write(f'{line.rstrip()[::-1]}\n')

reverse_line('input.txt','output.txt')