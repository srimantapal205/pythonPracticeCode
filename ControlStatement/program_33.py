#Program to display Finonacci series

n = int(input('How many Fibonaccis? : '))
f1 = 0 #this is first fibonacci number
f2 = 1 #this is first fibonacci number
c=2 #Count the no of fibonaccis
if n==1:
    print(f1)
elif n==2:
    print(f1,f2, sep='\n')
else:
    print(f1,f2, sep='\n')
    while c<n:
        f= f1+f2
        print(f)
        f1,f2 = f2,f
        c+=1