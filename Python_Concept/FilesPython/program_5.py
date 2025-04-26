#A python program to appent data an exiting file and then displaying the entire file
#appending and then reading strings
#open the file for reading data
f = open('myfile.txt', 'a+')
print(('Enter text to append (@ at end) :: '))
while str != '@':
    str = input() #accepting string in to str
    
    #write the string into file
    if(str != '@'):
        f.write(str+'\n')

#put the file pointer to the beginning of file
f.seek(0,0)

#read string from the file
print('The file contents are:: ')
str = f.read()
print(str)

#close file
f.close()
    