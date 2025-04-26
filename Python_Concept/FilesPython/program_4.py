#A python  to reade all the string from the text file and display them.
#reading string from a file
#open the file for reading data
f = open('groupline.txt', 'r')

#read string from the file
print('The file contents are :: ')
str = f.read()
print(str)

#close file
f.close()