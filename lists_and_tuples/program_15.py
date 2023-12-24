#A python program to find the first oceeurance of an element in tuple
#Inserting elements from keyboard as in to tuple and finding element position
#accept elements from keyboard as string seperated by commas
str = input('Enter elements seperated by commas :: ==  ').split(',')
lst = [int(num) for num in str] #Convert string into integers and store it into list
tup = tuple(lst) #Convert list into tuple

print('The tuple is :: ', tup)

ele = int(input('Enter an element to search:: '))
try:
    pos = tup.index(ele) #returns first occurance of element
    print('Element position no :: ', pos+1)
except: 
    print('Element not found')
