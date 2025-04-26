#A python program to know weather a file exit or not
#check if file exitis and then reading data
import os, sys

#open the file for reading data
fname = input ('Enter  file name :: ') 
if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname, 'does not exit!')
    sys.exit()

#read string from the file 
print("the file contents are ::: " )
str = f.read()
print(str)

#close file
f.close()

    