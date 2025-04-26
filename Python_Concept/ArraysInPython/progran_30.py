#A python program to alias an array and understand the affect of aliasing
from numpy import *
a = arange(1,6) #create element with 1-5
b =a #give another name b  to a

print("Original Array :: ", a)
print('Alias Array :: ', b)

b[0] = 99
print("\n After Modification of array :: \n")

print("Original Array :: ", a)
print('Alias Array :: ', b)
