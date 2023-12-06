#A python program to create a view() of an exiting array 
#Example of shallow copying

from numpy import *
a = arange(1, 6) #Create a with element 1 to 5
b = a.view() #Create a view of a and call it b

print("Original Array :: ", a)
print("New Array :: ", b)

b[0] = 99
print("\nModify 0th element of b\n")
print("Original Array :: ", a)
print("New Array :: ", b)

