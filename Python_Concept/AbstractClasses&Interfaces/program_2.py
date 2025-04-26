#A python program to create abstract class and subclass which implement the abstract method of the abstract class.
#abstract class example 

#from abc  import ABC, abstractmethod
from abc import *

class MyClass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass #empty body, on code
    

#this is sub class of myclass
class Sub1(MyClass):
    def calculate(self, x):
        #return super().calculate(x)
        print('The Squre value == ', x*x)

#this is another class fo MyClass
import math
class Sub2(MyClass):
    def calculate(self, x):
        print('Squre Root :: ', math.sqrt(x))

#the sub class for MyClass
class Sub3(MyClass):
    def calculate(self, x):
        print('Cube value == ', x**3)


#Create Sub1 class object and call calculate() method
obj1 = Sub1()
obj1.calculate(16)

#Create Sub1 class object and call calculate() method
obj2 = Sub2()
obj2.calculate(16)

#Create Sub1 class object and call calculate() method
obj3 = Sub3()
obj3.calculate(16)
    
    
    