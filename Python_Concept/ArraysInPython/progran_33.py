#A python program to understand slicing operation on array
from numpy import *
#create array a with element 10 to 16
a = arange(10, 17) 
print(a)

#retrive from 1st to one element prior to 6th element in steps of 2
b=a[1:6:2] # 1:Starting element, 6: stopning element, 2: steping element
print(b)

#retriving all element from array
b=a[::]
print(b)

#retriving from 6-2 =4th to one element to 2nd element in decreasing step size
b=a[-2:2:-1]
print(b)

#retriving from 0th to one element prior to 4th element (6-2=4th)
b=a[:-2:]
print(b)