#A python program to know how many times an element occurred in the list.
x = [] #take an empty list
n = int(input('How many elements ? '))
for i in range(n): #repeat for n times
    print('Enter element:: ', end='')
    x.append(int(input())) #the element to lis x

y = int(input('Enter element to count :: '))
c=0
for i in x:
    if(y==i):c+=1
print('{} is found {} times.'.format(y, c))

