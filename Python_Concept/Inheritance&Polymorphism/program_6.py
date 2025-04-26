#A python program to access the base class constractor from subclass
#base class constractor is vaailable to sub class

class Father:
    def __init__(self):
        self.property =8000000.00
    
    def display_property(self):
        print('Father\'s property :: ', self.property)
    
class Son(Father):
    pass #wedont want to write anything in the sub class

#Create a subclass instance and display father's property
s = Son()
s.display_property()


#The conclusion is that the constractors in the super class are also available to the sub class object.
        

        
        
        