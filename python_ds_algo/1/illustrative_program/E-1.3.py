#Write a program to compare the factorial of given number and display the result on the screen.
num = int(input('Enter the number: '))
fact = 1
for x in range(2, num+1):
    fact = fact * x

print(fact)

