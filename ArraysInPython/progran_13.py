#A python program to search for the position of an element in an array using index() method.
from array import *
#Create an empty array to store integer
x = array('i', [])
#Store elements into the array x
print('How many elements ?', end='')
n=int(input()) #accept input in to n

for i in range(n): #repeat for n times
    print('Enter Element :: ', end='')
    x.append(int(input())) #add elements into the array x
    
print('Original Array :: ', x)

print('Enter search element :: ', end='')
s= int(input()) #Accept element to be searched

#index() method give the location of the element in the array
try:
    pos = x.index(s)
    print('Found of the position = ', pos+1 )
except ValueError: #if element not found then valueerror will raise
    print('Not found in the array ')