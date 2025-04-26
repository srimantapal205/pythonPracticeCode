#A program to calculate  factorial value.
def fact(n):
    '''To find the factorial value'''
    prod =1
    while n>1:
        prod*=n
        n-=1
     #   print(n)
    #print(' :: ', prod)
    return prod

#Display factorial of first 10 numbers
#Call fact() function and pass the numbers from 1 to 10 for i in range(1, 11)
for i in range(1, 11):
    print('Factorial of {} is {}'.format(i, fact(i)))
