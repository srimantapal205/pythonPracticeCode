#Python program to search for the position of an element in an array using sequential search

from array import *
#Create an empty arry to store the integer
x =array('i',[])

#store element in to the array x
print("How many elements? ", end="")
n=int(input()) #accept input into n

for i in range(n):
    print('Enter element : ', end='' )
    x.append(int(input()))
print("Original Array: ", x)

print('Enter element to search :: ', end='')
s= int(input()) #accept element to searched 
#linear search or sequential search

flag = False #this become True if elemment is found 
for i in range(len(x)): #repeat i from 0 to no of element 
    if s == x[i]:
        print('Found at position= ', i+1)
        flag = True
if flag == False:
    print('Not found in the array')

        