#Find the sum of list of number using while loop
#Take a list of number
list = [10,20,30,40,50,60,70,80,90]
sum= 0 #initially sum is zero
i = 0 #take a varible

while i <len(list):
    print(list[i])
    sum+=list[i]
    i+=1
print('Sum= ',sum)
