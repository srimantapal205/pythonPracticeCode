# Write a Python program to calcute the Sine value of given angle in degrees by evaluating Sine series

#Accept user input
x,n=[int(i) for i in input('Enter angle value, no of iterations : ').split(',')]

#Convert the angle from degrees in to radians
r = (x*3.14159)/180

#this become first term
t=r

#till find the sum
sum = r

#Display the iteration number and sum
print('Iteration = %d\tSum=%f'%(1,sum))

#denominator for 2nd nth terms
i=2

#repeat for the 2nd nth terms

for j in range(2, n+1):
    t = (-1)*t*r*r/(i*(i+1))
    sum=sum+t
    print('Iteration = %d\tSum=%f'%(j,sum))
    i+=2