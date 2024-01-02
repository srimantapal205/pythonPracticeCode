#Inner  Class
#A python program to create Dob class within Person class
#Inner class example
class Person:
    def __init__(self) -> None:
        self.name ="Charles"
        self.dob = self.Dob()
    def display(self):
        print('Name: ', self.name)
        
    class Dob:
        def __init__(self) -> None:
            self.dd=10
            self.mm=5
            self.yyyy=1988
        def fdob(self):
            print('Dob : {}/{}/{}'.format(self.dd, self.mm, self.yyyy))
    

#Create Person class object
p = Person()
p.display()

#create inner class object
x =p.dob
x.fdob()