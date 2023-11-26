#To find sum of list of numbers using for.
#Take a list of numbers

list = [10,20,30,40,50]
sum= 0 #initially sum is zero
for i in list:
    print(i) #Display the element from list
    sum += i #add each element to sum
print('Sum= ', sum)