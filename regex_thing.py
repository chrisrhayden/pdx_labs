"""
Write functions that accept 'dirty' string input, and ouputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
'Beautiful is better than ugly.'

>>> gentle_clean('Explicit_is-better_than -implicit')
'Explicit is better than implicit.'

>>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex.'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently.'

>>> extracto('1S2pe3cia4l ca5ses ar6en\'t sp7ecial en8ough to b9reak the r0ules.')
45

>>> extracto('2S4pe6cia8l ca0ses ar2en\'t sp4ecial en6ough to b8reak the r0ules.')
40

>>> extracto('3S6pe9cia2l ca5ses ar8en\'t sp1ecial en4ough to b7reak the r0ules.')
45
"""
import re
import string

def scrub_numbers(phrase):
    rp = re.compile(r'''
                    \d
                    ''', re.VERBOSE)
    np = rp.sub('', phrase)
    np = np + '.'
    return np

def gentle_clean(phrase):
    regp = re.compile(r'''
                      (?<=\w)   # if a letter is behind
                      [_-]      # ether _ or -
                      (?=\w)    # if a letter is ahead
                      |         # or
                      \s        # space
                      -         # -
                      (?=\w)    # if a letter is ahead
                      ''', re.VERBOSE)
    clp = regp.sub(' ', phrase)
    clp = clp + '.'
    return clp


def clean_data(phrase):
    """
    >>> clean_data('  42Simple-is_better_than-compl9ex   ')
    'Simple is better than complex.'
    """
    rp = re.compile(r'''
                    \d   # all digits
                    ''', re.VERBOSE)
    regp = re.compile(r'''
                      (?<=\w)   # if a letter is behind
                      [_-]      # ether _ or -
                      (?=\w)    # if a letter is ahead
                      |         # or
                      \s        # space
                      -         # -
                      (?=\w)    # if a letter is ahead
                      ''', re.VERBOSE)
    ncp = rp.sub('', phrase)
    ncp = regp.sub(' ', ncp)
    ncp = ncp.strip()
    ncp = ncp + '.'
    return ncp

def some_scrubber(phrase):
    """
    >>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d .')
    'Flat is better than nested.'
    """
#    rp = re.compile(r'''
#                    (\s{1})   # only one space
#                    [^\s\s]   # not two spaces
#                    ''', re.VERBOSE)
#    #ncp = rp.sub('', phrase)
#    nrp = re.compile(r'''
#                     \s{3}   # match 3 spaces
#                     ''', re.VERBOSE)
    #ncp = re.split('\s{3}', phrase)
    #ncp.replace('  ', ' ')
    #rp = re.compile(r'''
    #                \s{1}      # all whit space
    #                (?=[^\b\s{3}])
    #                ''', re.VERBOSE)
    #ncp = rp.sub('', phrase)
    #ncp = ncp.replace('  ', ' ')
    ncp = phrase[::2]
    return ncp


def mr_clean(phrase):
    """
    >>> mr_clean('Sparse is better than dense')
    ' S p a r s e   i s   b e t t e r   t h a n   d e n s e '
    """
    ncp = [spar for spar in phrase]
    ncp = ' '.join(ncp)
    ncp = ' ' + ncp + ' '
    return ncp


def ms_clean(phrase):
    """
    >>> ms_clean('Readability counts')
    'R9y c4s'
    """
    ncp = ' '.join(f'{thi[0]}{len(thi[1:-1])}{thi[-1]}'
                   for thi in phrase.split())
    return ncp


def strong_cleaner(phrase):
    """
    >>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
    'Errors should never pass silently.'
    """
    pat = string.punctuation
    rp = re.compile(r'''
                    [\d''' +  pat + ''']
                    |
                    (?<=\S)
                    [A-Z]
                    (?=\S)
                    ''', re.VERBOSE)
    #ncp = re.sub(pat, '', phrase)
    ncp = rp.sub('', phrase)
    return ncp + '.'



def extracto(phrase):
#    """
#    >>> extracto('1S2pe3cia4l ca5ses ar6en\'t sp7ecial en8ough to b9reak the r0ules.')
#    45
#    """
    rp = re.compile(r'''
                    [a-zA-Z\.\']
                    ''', re.VERBOSE)
    ncp = rp.sub('', phrase)
    ncp = sum(int(num) for num in ncp if num is not ' ')
    return ncp




extracto('1S2pe3cia4l ca5ses ar6en\'t sp7ecial en8ough to b9reak the r0ules.')



