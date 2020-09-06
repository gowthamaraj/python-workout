'''
You’ll implement a translator from English into another secret children’s language, Ubbi Dubbi
(http://mng.bz/90zl). (This was popularized on the wonderful American children’s
program Zoom.) The rules of Ubbi Dubbi are even simpler than those of Pig Latin, although programming a translator is
more complex and requires a bit more thinking.
 In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes
mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am). In theory,
you only put an ub before every vowel sound, rather than before each vowel.
'''


def ubbi_dubbi(word: str)-> str:
    '''
    function to convert english to ubbi dubbi
    '''
    return ''.join([(f'ub{c}' if c in 'aeiou' else c)for c in word])

print(ubbi_dubbi('python'))