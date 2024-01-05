#A python programming to override super class constractor and method in sub class
#Overriding the base clas  constractor and method in sub class

class Father:
    def __init__(self):
        self.prperty =8000000.00

    def display_property(self):
        print('Father\'s property :: ', self.prperty)

class Son(Father):
    def __init__(self):
        self.prperty =2000000.00
    
    def display_property(self):
        print('Child\'s property :: ', self.prperty)

#Create subclass instance and display father's property

s = Son()
s.display_property()        
    
    