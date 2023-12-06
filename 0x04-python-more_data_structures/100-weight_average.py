#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculates the weighted average of a list of score-weight tuples.

    Args:
    my_list: A list of tuples containing integers (score, weight).

    Returns:
    The weighted average of the scores, or 0 if the list is empty.
    """

    if not my_list:
        return 0

    for tup in my_list:
        if not isinstance(tup[0], int) or not isinstance(tup[1], int):
            return 0

        num = 0
        den = 0

        for tup in my_list:
            num += tup[0] * tup[1]
            den += tup[1]

            return (num / den)
                                            
