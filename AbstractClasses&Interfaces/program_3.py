# A python program to create a car abstract class that contains an instance varible a concert method and two abstract class
#This is an abstract class.
from abc import *
class Car(ABC):
    def __init__(self, regno) :
        self.regno = regno

    def openTank(self):
        print('Fill the Fule into the tank')
        print('For the car with Reg No ::', self.regno)
    
    @abstractmethod
    def Steering(self):
        pass
    
    @abstractmethod
    def Braking(self):
        pass
    
    
        