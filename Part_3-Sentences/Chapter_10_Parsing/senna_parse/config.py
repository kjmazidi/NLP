# configuration file for senna_parser.py
# senna is a very fast SRL parser
# get senna here: http://ml.nec-labs.com/senna/

debug = True    # extra prints

# senna_dir = where the executable senna file is
# senna is the executable for your system
# you need to change senna_dir and senna for your system
# for my macbook:
senna_dir = '/Users/mazidi/toolbox/senna/'
senna = senna_dir+'senna-osx'  # for mac
# for my Surface Pro
#senna_dir = 'C:\\tools\\senna\\'
#senna = senna_dir+'senna-win32.exe'
# for my Ubuntu machine
#senna_dir = '/home/janice/toolbox/senna/'
#senna = senna_dir+'senna-linux64'

# input file
infile = 'in.txt'

# output file
outfile = 'senna.out'
