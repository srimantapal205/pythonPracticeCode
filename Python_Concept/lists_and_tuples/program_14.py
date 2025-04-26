#A python program to find the sum and avarage of elements in a tuple
num = eval(input('Enter elements in () :: ')) #Enter elements in () :: (10,20,30,40,50)
sum=0
n=len(num)
for i in range(n):
    sum += num[i]
print('The sum of numbers :: ', sum) #The sum of numbers ::  150
print('The avarage value of {} rlement is :: {}'.format(n, sum/n)) #The avarage value of 5 rlement is :: 30.0