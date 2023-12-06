#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
    roman_string: A string representing a Roman numeral.

    Returns:
    An integer representing the value of the Roman numeral.
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    for i in range(len(roman_string)):
        current_value = roman_numeral_map[roman_string[i]]
        if i + 1 < len(roman_string) and roman_numeral_map[roman_string[i + 1]] > current_value:
            result -= current_value
        else:
            result += current_value

            return result
                                      