# Demo two methods of making a file path cross-platform
# assumes sysarg is data/sample.txt


import sys  # to get the system parameter
import os   # used by method 1
import pathlib # used by method 2


def method1(filepath):

    print("\nUsing method 1")

    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    print(text_in)

def method2(filepath):

    print("\nUsing method 2")

    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        text_in = f.read()
    print(text_in)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        fp = sys.argv[1]
        method1(fp)
        method2(fp)