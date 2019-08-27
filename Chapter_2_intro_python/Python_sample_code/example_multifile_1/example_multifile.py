# Demo of a Python program using classes and configuration file
# Karen Mazidi
# July 2017

import example_multifile_config as config
from example_multifile_classes import Circle

def main():
    """Calculates area of circles.
"""

    # read in circle data
    with open(config.input_file) as f:
        lines = f.read().splitlines()

    # create a circle object for each circle
    circles = []
    for r in lines:
        c = Circle(r)
        c.calc_area()
        circles.append(c)

    # display circle data and write to file
    for c in circles:
        c.display()




if __name__ == "__main__":
    main()

