#Write a program to find the Cosin value of given angle in degrees by evLUting the cosine series.
#accepting  user input
x,n = [int(i) for i in input('Enter angle value, no. of iterations : ').split(',')]

#convert the angle from degrees into radians
r=(x*3.14159)/180

#this becomes the first term
t=1

#till now, sum is 1 only
sum=1

#display the iteration number and sum
print('Iteration = %d\tSum=%f' %(1, sum))

#denominator for the second term
i=1

#repeat for the second term
i=1

#repeat for 2nd to nth terms

for j in range(2, n+1):
    t=(-1)*t*r**2/(i*(i+1)) #find the next term
    sum=sum+t #add it to sum
    print('Iteration=%d\tSum= %f' %(j,sum))
    i+=2 #increase i value by 2 for denominator for next term