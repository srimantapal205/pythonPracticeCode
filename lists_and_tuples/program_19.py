#A program to delete an element from a particuler position in the tuple
#delete an element of tuple
num = (10,20,30,40,50,60)
print(num)

#accept position number of the element to delete 
pos = int(input('Enter position no :: '))

#copy from 0th to pos-2 into another tuple num1
num1 = num[0:pos-1]

#concatenate the remaining elements of num from pos till end 
num = num1+num[pos:]
print(num)

