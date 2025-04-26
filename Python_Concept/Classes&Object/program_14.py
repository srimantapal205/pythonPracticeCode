#Inner class example v2
class Person:
    def __init__(self) -> None:
        self.name = 'Charls'
    
    def display(self):
        print('Name : ', self.name)
    
    class Dob:
        def __init__(self) -> None:
            self.dd=10
            self.mm=5
            self.yy=1988

        def fullDob(self):
            print('DOB : {}/{}/{}'.format(self.dd, self.mm, self.yy))


#Create Person class object
p = Person()
p.display()
#Create Dob class object as sub object to person class
pdob = Person().Dob()
pdob.fullDob()

print(pdob.yy)