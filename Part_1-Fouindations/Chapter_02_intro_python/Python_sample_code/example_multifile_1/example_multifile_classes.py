# example class file with class variables and method

import math

class Circle():

    def __init__(self, radius):
        self.radius = float(radius)
        self.area = 0

    def display(self):
        print('Radius = {:.2f} Area = {:.2f}\n'.format(self.radius, self.area))

    def calc_area(self):
        self.area = math.pi * math.pow(self.radius, 2)