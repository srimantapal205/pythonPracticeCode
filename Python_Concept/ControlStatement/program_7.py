#A given number is zero of +ve or -ve
num = int(input('Enter a number: '))
if num == 0:
    print(num, " is zero")
elif num>0:
    print(num, " is positive")
else:
    print(num, " is negative")