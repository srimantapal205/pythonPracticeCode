#Apython program to modify or replace an exiting element of a tuple with a new element
#modifying an exiting element of a tuple
num = (10,20,30,40,50,60)
print(num)

#Accept new element and position number
lst = [input('Enter a new element :: ')]
new = tuple(lst)
pos = (int(input('Enter the position no ::')))

#Copy from 0th to pos-2 in to another tuple num1
num1 = num[0:pos-1]

#Concatenate new element at pos-1
num1 =num1+new

#concatenate the reamining elements of num from pos till end 
num = num1 + num[pos:]
print(num)