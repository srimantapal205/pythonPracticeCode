#A Python program to override the super class method is sub class
#method overriding
import math
class Squre:
    def area(self, x):
        print('Squre area = %f}'%x*x)
    
class Circle(Squre):
    def area(self, x):
        print('Circle area = %.4f'%(math.pi*x*x))

#call area() using sub class object
c = Circle()
c.area(15)

