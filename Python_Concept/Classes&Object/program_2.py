#A python program  to create Student class with a constractor having more than one parameter
#instance vars and instance methos -- v2
class Student:
    #this is constractor
    def __init__(self, n='', m=0):
        self.name = n
        self.markes = m

    #this is an instance method.
    def display(self):
        print('Hi ', self.name)
        print('Your markes: ', self.markes)
    
#Constractor is called without any arguments
s = Student()
s.display()
print('-------------------------------------')

#Constractoor is called with 2 arguments
s1 = Student('Lakshmi Roy', 880)
s1.display()        
print('-------------------------------------')        