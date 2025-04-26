#A python program to reade character form a text file
#read character from file
#open the file for reading the file
f = open('myfile.txt', 'r')

#read all character from file
rstr = f.read()

#display them on the screen
print(rstr)

#close file
f.close()