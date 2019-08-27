# Demo of a simple Python program
# Karen Mazidi
# July 2017

import sys

def main():
    """Displays some information about an input string.

    Input string can come from 2 sources:
        - a sys.argv if present
        - a default string if there is no sys.argv
    """

    if len(sys.argv) > 1:
        arg_input = sys.argv[1]
        print('Input string: ', arg_input)
        result = count_string(arg_input)
        print('result using arg input = ', result)
    else:
        default_input = 'CS 4301 Natural Language Processing'
        print('Default string: ', default_input)
        result = count_string(default_input)
        print('result using default input = ', result)


def count_string(str1):
    """Counts the number of non-space and space characters in a string.
    Args:
        str1 (string): input string

    Returns:
        int: count of non-space characters in str1
        int: count of spaces in str1
    """
    num_spaces = str1.count(' ')
    return len(str1) - num_spaces, num_spaces

if __name__ == "__main__":
    main()

# Some commentary:
# the Python interpreter sets the __name__ variable to __main__ if it is a standalone program
# otherwise it sets __name__ to the name of the module
# so if you run this script like this: python3 main_example.py
#    then all of the code at indentation level 0 gets executed,
#    including the above 'if' which calls main()
