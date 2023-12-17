#A python program to calculate factorial value using recursion
#recursive function to calculate the factorial 
def factorial(num):
    '''to find the factorial value of num'''
    if num==0:
        res = 1
    else:
        res = num*factorial(num-1)

    return res

#find the factorial values for first 10 numbers
for i in range(1, 11):
    print('Factorial of {} :: {}'.format(i, factorial(i)))
    
    
    