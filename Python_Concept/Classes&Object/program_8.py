#Static Methods
#A pyhon program to create a static method that count the number of instance created myclass
#Understanding the static methods
class MyClass:
    #This is class var or Static var
    n=0
    #constructor that increments n when an instance is created 
    def __init__(self):
        MyClass.n = MyClass.n+1
    
    #this is astatic method to display the no of instance
    @staticmethod
    def noobject():
        print('No. of instance created  :: ', MyClass.n)
        
#create 3 instance
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
MyClass.noobject()            
        
