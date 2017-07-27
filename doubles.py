"""

#  Leave the line below alone, it is test data.
>>> llamas = [45, 37, 96, 23, 55, 2, 0, 88, 0, 45, 0, 345, 1, 76, 45, 34, 87]

>>> apply_to_all(llamas, 2)
[90, 74, 192, 46, 110, 4, 176, 90, 690, 2, 152, 90, 68, 174]

"""


from typing import List


def apply_to_all(i_list: List[int], n: int) -> List[int]:
    """ multiply all ints in a list """

    sum_nums = [(num * n) for num in i_list if num * n > 0]
    return sum_nums
