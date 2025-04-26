#A python program to access base class constractor and methods in the sub class using super()
#Accessing base class constractor and method in the sub class

class Squre:
    def __init__(self, x):
        self.x = x
    
    def area(self):
        print('Area of squre :: ', self.x*self.x)
    

class Rectangle(Squre):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    
    def area(self):
        super().area()
        print('Area of Rectangle == ', self.x*self.y)

#find areas of square an rectangle

a, b = [float(x) for x in input('Enter two measuerments :: ').split(',')]

r = Rectangle(a,b)
r.area()

         

