# example class file with class variables and method

import math


class Circle:

    def __init__(self, radius):
        self.radius = float(radius)
        self.area = 0

    def display(self):
        print(f'Radius = {self.radius:.2f} Area = {self.area:.2f}\n')

    def calc_area(self):
        self.area = math.pi * math.pow(self.radius, 2)