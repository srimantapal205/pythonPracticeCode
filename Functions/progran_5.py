#A python function to test  whether a number is prime or not
def prime(n):
    '''To checkif a number is prime or not'''
    x = 1 #this will be 0 if not prime
    for i in range(2, n): #Divide from 2 to n-1
        if n%i == 0:
            x= 0 #Take x as 0
            break
        else:
            x = 1 #else take x as 1
    return x 
    
#Test if a number is prime or not
num = int(input("Enter a number :: "))

#check if num is prime or not
result = prime(num)

if result == 1:
    print(num, ' :: is prime')
else:
    print(num, ' :: is not prime')