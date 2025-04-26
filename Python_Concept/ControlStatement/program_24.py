#Using break to come out of while loop
x= 10
while x>=1:
    print('x : ', x)
    x-=1
    if x==5:  # if x is 5 the come out from while loop
        break
else:
    print("Out of the loop")