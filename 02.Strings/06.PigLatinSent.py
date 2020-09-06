'''
Now that you’ve successfully written a translator for a single English word, let’s make
things more difficult: translate a series of English words into Pig Latin. 
Write a function called pl_sentence that takes a string containing several words, separated by
spaces.
'''

def pl_sentence(sentence: str)-> str:
    words = sentence.split(' ')
    output = []
    for word in words:
        if word[0] in 'aeiou':
            output.append(f'{word}way')
            continue
        output.append( f'{word[1:]}{word[0]}ay')
    return ' '.join(output)


print(pl_sentence('this is a test'))