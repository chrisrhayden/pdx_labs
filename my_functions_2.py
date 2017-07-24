"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""


def combine(num1: int, num2=0) -> int:
    """ combine 1 or 2 ints """

    sum_nums = num1 + num2
    return sum_nums


def combine_many(*nums: int) -> int:
    """ get parse and sum args """

    sum_nums = sum(nums)
    #sum_nums = int()
    #for num in nums:
    #    sum_nums += num
    return sum_nums


def choose_longest(*thigs):
    """ get names and return the longest """

    long_thing = max(thigs, key=len)
    return long_thing



#choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
#combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
#@print(combine(1, 2))
