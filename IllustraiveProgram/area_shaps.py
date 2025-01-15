# Write a program to compute the area of diffrent shapes and display the information on teh screen.

import math
radius = float(input('Enter the radius: '))
pi = math.pi

areaCircle = pi*radius**2
print(areaCircle)

rect = input('Enter the Length and Breadth of a rectangle separated by space :: ')
length = float(rect.split()[0])
breadth = float(rect.split()[1])
areaRect = length*breadth
print(areaRect)

 
