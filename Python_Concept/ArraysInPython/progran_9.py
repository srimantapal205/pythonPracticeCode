#Write a program to understan various methods of a arrays class
from array import *
#Create an array with int values
arr = array('i', [10,20,30,40,50,60,70,80,90])
print('Original Array :: ', )
for element in arr:
    print(element, end=" ")
 
#Append 100 to the array
arr.append(100)
arr.append(110)
print('\n\nAfter appending the 100 and 110 :: ')
for el in arr:
    print(el, end=' ')

#insert 00 at the position number 1 in arr
arr.insert(0,00)
print('\n\nAfter insert 00 in first position :: ')
for el2 in arr:
    print(el2, end=" ")

#Remove an element from arr
arr.remove(100)
print('\n\nAfter removed 100 the new array :: ')
for el3 in arr:
    print(el3, end=" ")

#Remove last element using pop() method
n =arr.pop()
print('\n\nAfter using pop() new array :: ')
for el4 in arr:
    print(el4, end=" ")
print('\nRemoved Item is :: ', n)

#Finding the position of element using index method
un = int(input('\n\nEnter one value from arry :: '))
np = arr.index(un)
print('Position of {} in the array is :: {}'.format(un,np))

#Conver an array into a list using tolist() method
lst = arr.tolist()
print('\nList :: ', lst)
print('Array :: ', arr)


