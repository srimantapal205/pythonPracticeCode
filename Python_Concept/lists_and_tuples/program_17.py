#A python program to insert a new element into a tuple of elements at a specified position
#Insert a new elements in to a tuple
names = ('Visnu','Anupama','Lakshmi','Bheeshma')
print(names)
#Accept new name and position number
lst =[input('Enter a new name:: ' )]
new =tuple(lst)
pos = int(input('Enter the position no :: '))

#copy 0th to pos-2 in to another tuple names1
names1 = names[0:pos-1]

#concatenate new element at pos-1
names1=names1+new

#Concatenate the remaining elements of names from pos-1 till end 
names = names1+names[pos-1:]
print(names)