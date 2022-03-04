"""
Module docstring Information what does this module,
This is a simulation of how long did we have to draw to win max price in Lotto
"""
from random import randint


def draw_numbers() -> object:
    """
    Draw 6 numbers without duplication in range 1 to 49
    Return list : list containing 6 digits in range 1:49 without duplication
    """
    drew = []
    while len(drew) < 6:
        get_number_in_range = randint(1, 49)
        if get_number_in_range not in drew:
            drew.append(get_number_in_range)
    return drew


def iterate_until_equal(my_set, drawing_number_algorithm):
    """
    While loop returning numbers of try to draw numbers. We assume if won in first time it is in week 1 not a week 0
    :param drawing_number_algorithm: is algorythm to check data
    :param my_set: set contains numbers without duplicates
    :return: counter(int): counter with number of try
    """
    count = 1
    while my_set != set(drawing_number_algorithm()):
        count += 1
    return count


if __name__ == '__main__':
    MY_SET = {1, 13, 17, 9, 49, 21}
    # We assume is one draw per week
    COUNT_WEEKS = iterate_until_equal(MY_SET, draw_numbers)
    print(f'Udało się, potrzeba było {COUNT_WEEKS} tygodni,'
          f' czyli {COUNT_WEEKS // 52} lat i {COUNT_WEEKS % 52} tygodni')
