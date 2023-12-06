#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculates the weighted average of a list of score-weight tuples.

    Args:
    my_list: A list of tuples containing integers (score, weight).

    Returns:
    The weighted average of the scores, or 0 if the list is empty.
    """

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        if isinstance(score, int) and isinstance(weight, int):
            total_score += score * weight
            total_weight += weight
        else:
            print(f"Warning: Invalid data type: {(score, weight)}")

            if total_weight == 0:
                return 0

            return total_score / total_weight
