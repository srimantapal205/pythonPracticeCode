#A python program to find the maximum and minimum elements in a list of elements
#find bigest and smallest element in a list of numbers

x = [] #take a empty list
print('How amny element :: ', end=' ')
n = int(input())

for i in range(n): #repeat for n times
    print('Enter element :: ', end=' ')
    x.append(int(input())) #add the element in the list
     
print('The list is :: ', x)

big = x[0] #initially 0th element becomes maximum and minimum 
small=x[0]

for i in range(1, n):
    if x[i]>big: big =x[i] #if any other elements is big, take it as big 
    if x[i]<small : small=x[i]#if any other elements is small, take it as small 

print('Maximum is :: ', big)
print('Minimum is :: ', small)

'''Using the max() and min ()'''
maxValue = max(x)
print('Maximum value using by max() :: ', maxValue)

minValue = min(x)
print('Minimum value using by min() :: ', minValue)
