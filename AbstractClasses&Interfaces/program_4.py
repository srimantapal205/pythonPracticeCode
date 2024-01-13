#A python program in which Maruti subclass implement the abstract method of the super class Cars
#This is a sub class for abstract Cars class
from program_3 import Cars
class Maruti(Cars):
    def steering(self):
        print('Maruti uses manual steering')
        print('Drive the car')
    
    def braking(self):
        print('Maruti uses hydraulic brakes')
        print('Apply brake and stop its')
    
#Create Object to maruti and use it features
m = Maruti(123456)
m.openTank()
m.steering()
m.braking()