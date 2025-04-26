#Create a python program  to Create one array from another array
from array import *
arr1 = array('d',[1.2,2.5,-3.5,4])
#Use same type code and multiply each element of arr1 with 3
arr2 = array(arr1.typecode, (a*3 for a in arr1))
print('The array 2 elements are :: ')
for element in arr2:
    print(element)
 