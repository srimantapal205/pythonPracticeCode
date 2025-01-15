#Write a program to compute the factorial of given number and display the result on the screen

num = int(input('Enter the Number:: '))
fact = 1
for x in range(2, num+1):
    fact = fact * x
    print(fact, end=', ' )
print('\nThe Factorial Value = :: ',fact)