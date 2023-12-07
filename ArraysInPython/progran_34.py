#A python program to retrive and display elements of numpy array using indexing
from numpy import *
#create array with elements 10 to 16.
a=arange(10, 16)
print(a)

#retriving 1st to one element prior to 6th elemen in step of 2
a=a[0:5:1]
print(a)

#display element using index
i=0
while(i<len(a)):
    print(a[i])
    i+=1