#Write a program to check if a given number is prime and display the result on the screen

num = int(input('Enter the number : '))

import math
prime = True
x = int(math.sqrt(num))
while x>1:
    if num%x == 0:
        print(x, 'divides', num)
        prime = False
        break
    else:
        x -= 1

if prime:
    print('The number', num, 'is prime')
else:
    print('The number', num, 'is NOT prime')

