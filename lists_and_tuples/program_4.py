#A python program to display the element of a list in reverse order
#displaying list element in reverse order
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
for i in days:
    print(i)

print('\nIn reverse order:: ')

i = len(days) -1 #I will be 4
while i>=0:
    print(days[i]) #Display from 4th to 0th elements
    i-=1

print('\nIn reverse order :: ')
i=-1
while i>=-len(days): #represent last elements
   print(days[i]) #Display from -1 th to -5th elements
   i-=1
    
