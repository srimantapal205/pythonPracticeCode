#A python program to call the super class constractor in the sub class using super()
#Accessing base class constractor in sub class
class Father:
    def __init__(self, property=0):
        self.property =property
    
    def display_property(self):
        print('Father\'s property', self.property)
    
class Son(Father):
    def __init__(self, property=0, property1=0):
        super().__init__(property)
        self.property1 = property1
    
    def display_property(self):
        print('Total property child:: ', self.property1+self.property)

#Create sub class instance and display Father property

s = Son(2000000.00, 8800000.50)
s.display_property()


    
