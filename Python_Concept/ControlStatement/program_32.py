#Program to print numbers upto a given number
#accept upto what number the user wants

max = int(input("Upto what number? : "))
for num in range(2, max+1): #Generate from 2 onword till max
    for i in range(2,num): #i represent numbers from 2 num-1, 
        if (num % i) == 0: #if num is divisible by i then it is not prime , hence go back and check next number
            break 
    else:
        print(num) #otherwise it is a prime and hence display 