"""

>>> numbers = [2, -4, -6, 7,-9, 1, 9, -2, -3, 6]

>>> quote = "In the end, it's concluded that the airspeed velocity of a (European) unladen swallow is about 24 miles per hour or 11 meters per second. But, the real question is not about swallows at all."

>>> sorted_absolute(numbers)
[1, 2, -2, -3, -4, -6, 6, 7, -9, 9]

>>> shortest_to_longest(quote)
['a', 'In', 'of', 'is', '24', 'or', '11', 'is', 'at', 'the', 'the', 'per', 'per', 'the', 'not', 'end,', "it's", 'that', 'hour', 'But,', 'real', 'all.', 'about', 'miles', 'about', 'meters', 'unladen', 'swallow', 'second.', 'airspeed', 'velocity', 'question', 'swallows', 'concluded', '(European)']

>>> sort_last_char(quote)
['(European)', 'end,', 'But,', 'second.', 'all.', '11', '24', 'a', 'concluded', 'airspeed', 'the', 'the', 'the', 'of', 'real', 'In', 'unladen', 'question', 'per', 'hour', 'or', 'per', "it's", 'is', 'miles', 'meters', 'is', 'swallows', 'that', 'about', 'not', 'about', 'at', 'swallow', 'velocity']

>>> double(numbers)
[4, -8, -12, 14, -18, 2, 18, -4, -6, 12]

>>> all_upper(quote)
['IN', 'THE', 'END,', "IT'S", 'CONCLUDED', 'THAT', 'THE', 'AIRSPEED', 'VELOCITY', 'OF', 'A', '(EUROPEAN)', 'UNLADEN', 'SWALLOW', 'IS', 'ABOUT', '24', 'MILES', 'PER', 'HOUR', 'OR', '11', 'METERS', 'PER', 'SECOND.', 'BUT,', 'THE', 'REAL', 'QUESTION', 'IS', 'NOT', 'ABOUT', 'SWALLOWS', 'AT', 'ALL.']

>>> positive(numbers)
[2, 7, 1, 9, 6]

Filter words longer than 3, make all words lowercase words,
and sort by last letter.
>>> lower_last_longwords(quote)
['(european)', 'end,', 'but,', 'second.', 'all.', 'concluded', 'airspeed', 'real', 'unladen', 'question', 'hour', "it's", 'miles', 'meters', 'swallows', 'that', 'about', 'about', 'swallow', 'velocity']

"""


def sorted_absolute(numbers: list) -> list:
    sort_num = [snum for snum in numbers]
    sort_num.sort(key=abs)
    return sort_num


def shortest_to_longest(quote: str) -> list:
    split_q = quote.split(' ')
    clean_quote = list(filter(None, split_q))
    clean_quote.sort(key=len)
    return clean_quote


def sort_last_char(quote: str) -> list:
    split_q = quote.split(' ')
    clean_quote = list(filter(None, split_q))
    clean_quote.sort(key=lambda cl: cl[-1])
    return clean_quote


def double(numbers: list) -> list:
    _nums = [num*2 for num in numbers]
    return _nums


def all_upper(quote: str) -> list:
    sp_quote = quote.split(' ')
    cl_quo = list(filter(None, sp_quote))
    up_quo = [uquote.upper() for uquote in cl_quo]
    return up_quo


def positive(numbers: list) -> list:
    pos_num = [num for num in numbers if num > 0]
    return pos_num


def lower_last_longwords(quote: str) -> list:
    sp_quote = quote.split(' ')
    l_l_l = [lllword.lower() for lllword in sp_quote if len(lllword) > 3]
    l_l_l.sort(key=lambda lch: lch[-1])
    return l_l_l
