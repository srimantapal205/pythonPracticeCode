#To display even number between two value

m,n =[int(i) for i in input("Enter minimum and maximum range : ").split(',')]
x=m #start from m on word
if x%2 != 0: #if x is not even, start from next number
    x=x+1

while x>=m and x<=n:
    print(x)
    x+=2
