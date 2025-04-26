#A python program to store a group of string in the text file 
#Create a file with strings
#open the file for writing data
f = open('groupline.txt', 'w')
#ensure string from keyboard.
print('Enter text  (@ at end) :: ')
while str !='@':
    str = input() #accept string into str
    #write the string into file
    if(str != '@'):
        f.write(str+'\n')
    
#close the file
f.close()