#Create a python program that generate prime number 
def genPrime(n):
    '''to check if n is prime or not'''
    x = 1 #this will be 0 if not prime
    for i in range(2, n):
        if n%i ==0:
            x=0
            break
        else:
            x=1
    return x

num = int(input("How may prime number you want :: "))
i = 2 # start with i value 2
c = 1 #this counts the no of primes

while True:
    if genPrime(i):
        print(i) 
        c+=1#increase counter
    i+=1
    if c>num: #if count exceed num
        break #come out the while loop

