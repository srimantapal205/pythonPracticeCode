#Creating a array using logspace
from numpy import *

#Divide the range : 10 power 1 to 10 power 4 into 5 equal parts and take those points in the array
a= logspace(1, 4, 5)

#find the number of elements in a 
n =len(a)
print('Len :: ',n)

#repeat 0 to n-1 times
for i in range(n):
    print('%.1f' % a[i], end=' ') #display 1 digit after decimal point
     