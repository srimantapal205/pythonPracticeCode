#A python program to retrive the elements from 2D array and display them using for loop
from numpy import *
#Creat a 2D array with 3 rows array and 3 column
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#display only rows
for i in range(len(a)):
    print(a[i])

#display element by element

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
