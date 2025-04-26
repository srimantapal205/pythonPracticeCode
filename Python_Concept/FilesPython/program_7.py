#A python program to read the file and count number of line, word and characters in the text file.
#Read file, count number of line , word and character in the file.
import os, sys

#open the file for reading data
fname = input('Enter the file name :: ')

if os.path.isfile(fname):
    with open(fname, 'r') as f:
        content = f.read()
        print(content)
else:
    print('The file does not exit')
    sys.exit()

#initialize the countters to 0
cl = cw = cc = 0

#read line by  line from the file
#for line in content.splitlines():
for line in content.split('\n'):
    word = line.split()
    cl += 1
    cw += len(word)
    cc += len(line)

print('No of line :: ', cl)
print('No of word :: ', cw)
print('No of characters :: ', cc)

#close file
f.close()

