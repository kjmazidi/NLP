# Homework 0 Sample Solution
# Karen Mazidi
# July 2017

import homework1_config as config
from homework1_classes import Person

def main():
    """Calculates BMI from user data.
    """

    with open(config.input_file) as f:
        lines = f.read().splitlines()

    person_list = []
    for line in lines:
        name, height, weight = line.split()
        person = Person(name, height, weight)
        person.calc_bmi()
        person_list.append(person)


    # display persons
    f = open(config.output_file, 'w')
    for person in person_list:
        person.display()
        f.write('%-12s %2.1f %s \n' % (person.name, person.bmi, person.message))

    f.close()




if __name__ == "__main__":
    main()

