#A python program to access list elements using loops
#Dispaly list elements using while end for loops
lst =[10,20,30,40,50,60]
print('Using while loop:: ')
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
    
print('Using for loop :: ')
for i in lst: print(i)