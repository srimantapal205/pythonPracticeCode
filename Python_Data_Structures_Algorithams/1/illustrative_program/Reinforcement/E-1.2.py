#Write a program to compare the area of diffrent shape and display the informationon the screen.

radius = float(input('Enter the radious : '))
import math
pi = math.pi
areaCircle = pi*radius**2
print(areaCircle)

rect = input('Enter the length and breadth of rectangle separated by space : ')
length = float(rect.split()[0])
breadth = float(rect.split()[1])
areaRect = length*breadth
print(areaRect)
