#todisplay command line args. save this as cmd.py.

import sys

n = len(sys.argv) # n is number of arguments
args = sys.argv #args list contains arguments
print("No. of command line argument: ", n)
print("The arg are: ", args)
for a in args : 
    print(a)
