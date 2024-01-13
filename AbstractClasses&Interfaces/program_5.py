#A python program  in which for abstract class Cars classes

from program_3 import Cars

class Santro(Cars):
    def steering(self):
        print('Santro use power steerring')
        print('Drive the car')
    
    def braking(self):
        print('Santo use gas brakes')
        print('Apply brakes and stop it')
    
#create object to santro and use its feature

s = Santro(78789)
s.openTank()
s.steering()
s.braking()
