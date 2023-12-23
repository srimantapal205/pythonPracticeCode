#A python program to create a nested list and  display it's elements
lst1 =[10,20,30]
lst2 =[40,50]
newLst = [60,70,lst1,lst2]

print('Total list :: ', newLst) #Display entire list 
print('First element :: ', newLst[0]) #display first element
print('Last element :: ', newLst[3])

for x in newLst[3]:
    print(x)
    
    

