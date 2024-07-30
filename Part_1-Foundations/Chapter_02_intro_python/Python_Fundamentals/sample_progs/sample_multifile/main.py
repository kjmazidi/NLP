# Demo of a Python program using classes and configuration file
# Karen Mazidi
# April 2020

import config as config
from class_def import Circle


def calc_area(rads):

    # create a circle object for each circle
    circles = []
    for r in rads:
        c = Circle(r)
        c.calc_area()
        circles.append(c)

    return circles


if __name__ == "__main__":

    # read in circle data
    with open(config.input_file) as f:
        lines = f.read().splitlines()

    circle_list = calc_area(lines)

    # display circle data and write to file
    for c in circle_list:
        c.display()





