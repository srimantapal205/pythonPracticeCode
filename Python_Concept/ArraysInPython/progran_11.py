#A program to sort the array elements using bubble sort technique
from array import *
#Create an emplt array to store the intigers
x = array('i', [])

#store element in to the array x
print('How many Element ?? ', end='')
n = int(input()) #accept input into n

for i in range(n): # repeat for n times
    print('Enter Element: ', end='')
    x.append(int(input())) #add element into the x array

print('Original array : ', x)

# bubble sort
flag = False #when swapping in done flaf become True
for i in range(n-1): #i is from 0 to n-1
    for j in range(n-1-i): #j is from 0 to one element lesser than i
        if x[j] > x[j+1]: #if first element is bigger than the second element
            t = x[j] #Swap j and j+1 elements
            x[j] = x[j+1]
            x[j+1]=t
            flag= True #Swapping done, hence flaf is true
    if flag == False: #no swapping means array is in stored order
        break #Come out of the inner loop
    else:
        flag = False #Assign initial value to flag
print('Sorted array :: ', x)
    

    