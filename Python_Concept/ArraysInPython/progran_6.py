# A Python program to retrive elements of an array using while loop
from array import *
x = array('i', [10,20,30,40,50,60,70,80,90])

#Find the number of element in the array

n = len(x)
print("The number of length :: ", n)

#Display array elements using indexing
z = 0
while z<n:
    print(x[z], end=" ")
    z+=1
    