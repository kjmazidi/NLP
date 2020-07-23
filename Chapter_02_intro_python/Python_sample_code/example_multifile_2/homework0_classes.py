# classes for Homework 1

class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
        self.bmi = 0
        self.message = 'none'

    def display(self):
        print("\n ", self.name)
        print("\t bmi =  ", self.bmi)
        print("\t", self.message)

    def calc_bmi(self):
        self.bmi = (703 * self.weight) / (self.height * self.height)
        if self.bmi < 18.5:
            self.message = 'underweight'
        elif self.bmi < 25:
            self.message = 'normal weight'
        elif self.bmi < 30:
            self.message = 'overweight'
        else:
            self.message = 'obese'
