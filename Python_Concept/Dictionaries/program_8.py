#A python program to sort the elements of dictionary based on a key or value 
#Sorting a dictionary by key or value 
#take a dictionary
colors ={10:'Red', 15:'Green', 35:'Orange', 20:'Blue', 25:'White', }

#Sorted dictionary by key
print('Item Soorted By Key')
clrSortedByKey = sorted(colors.items(), key = lambda t:t[0])
print(clrSortedByKey)

#Sorted dictionary by items
clrSortedByValue = sorted(colors.items(), key=lambda t: t[1])
print('Item Soorted By Value')
print(clrSortedByValue)

