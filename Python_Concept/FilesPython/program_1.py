#A python program to createa text file to store individual characters
#create a file to store characters
#Open the file for writing data
f = open('myfile.txt', 'w')

#Enter character form keyboard
wstr = input('Enter text :: ')

#write the string in to file
f.write(wstr)

#close the file
f.close()
