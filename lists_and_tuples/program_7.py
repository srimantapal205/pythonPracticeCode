#A python program to sort the list elements using bubble sot technique.
#sorting is list using bubble sort technique
#Create an empty list to store integers
x = []
#store elements into the list x
print('How many elements ? ', end='')
n = int(input()) #accept input into n

for i in range(n): #repeat for n times
    print('Enter elements :: ', end='')
    x.append(int(input())) #add the element to the list x
    
print('Original list :: ', x)
num = x
print(num)

#bubble sort
flag = False #when swapping is done, flag becomes True
for i in range(n-1):#i is from 0 to n-1
    for j in range(n-1-i): #j is from 0 to one element leasser then i
        if x[j] > x[j+1]: #if 1st element is bigger than 2nd one 
            t = x[j] #swap j and j+1 elements
            x[j] = x[j+1]
            x[j+1] = t
            flag = True#swapping done, hence flag is true
    if flag == False:#no swapping means list is in sorted order
        break #come out the inner loop 
    else:
        flag == False #Assign initial value to flag
print(x)   

''' using sort() method to sort the elements''' 
#newSort = num.sort(reverse=True)
newSort = num.sort()
print('The sort elements :: ', newSort)

    