#A python program to create a copy() of an exiting array 
#Example of deep copying

from numpy import *
a = arange(1, 6) #create  a with element 1 to 5
b = a.copy() #Create a copy of and call it b

print('Original array :: ', a)
print('New array :: ', b)

b[0]=99
print('\n Ater modification ::\n')
print('Original array :: ', a)
print('New array :: ', b)


