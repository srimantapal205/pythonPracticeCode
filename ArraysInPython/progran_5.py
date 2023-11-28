#Write aprogram to retrive the element of an array using array index
from array import *
x = array('i', [10,20,30,40,50,60,70,80,90])

#find nub=mber of elements in the array
n = len(x)
print('Array length:: ', n)
#Display array elements using indexing
for i in range(n): # repeat from 0 to n-1
    print(x[i], end=' ')