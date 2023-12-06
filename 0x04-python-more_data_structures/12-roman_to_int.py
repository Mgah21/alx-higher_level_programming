#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
    roman_string: A string representing a Roman numeral.

    Returns:
    An integer representing the value of the Roman numeral.
    """

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    previous_value = 0

    for char in roman_string:
        current_value = roman_map[char]
        if previous_value < current_value:
            result -= previous_value * 2
        else:
            result += current_value
            previous_value = current_value

            return result
