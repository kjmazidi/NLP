# Demo of a simple Python program
# Karen Mazidi
# May 2020

import sys


def count_e(string_in):
    """Counts the number of 'e' letters in a string.

    Args: string_in is a string

    Returns: count, an integer count of the number of es in a string

    """

    # disclaimer: there are smarter ways to do this
    #    which we will discuss when we get to the Strings video
    count = 0
    for letter in string_in:
        if letter == 'e':
            count += 1

    return count


if __name__ == "__main__":
    """
    Input string can come from 2 sources:
        - a sys.argv if present
        - a default string if there is no sys.argv
    """

    if len(sys.argv) > 1:
        arg_input = sys.argv[1]
        print('Input string: ', arg_input)
        result = count_e(arg_input)
        print('result using arg input = ', result)
    else:
        default_input = 'this is a default string'
        print('Default string: ', default_input)
        result = count_e(default_input)
        print('result using default input = ', result)



