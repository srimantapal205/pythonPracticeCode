#Write a program  to evalute exponential series
#Accepting user input
x,n =[int(i) for i in input("Enter power of e, no of terations : ").split(',')]

#this is the first term
t=1

#till now sum is 1 only
sum = t

#Display the iteration number and sum
print('Iteration = %d\t Sum = %f'%(1,sum))

#repeat for 1st  to n-1th terms
for j in range(1, n):
    t= t * x/j #Find the next term
    sum=sum+t #Add it to sum
    print('Iteration = %d\t Sum = %f' %(j+1,sum))
