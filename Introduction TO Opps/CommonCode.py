#Introduction of OPPS

#Creating a class and object in python
#this is a class
#
class Persion:
    
    #attributes means varibles
    name  = 'Raju'
    age =20
    
    #action means functions
    def talk(cls):
        print(cls.name)
        print(cls.age)

p1 = Persion()    


#Encapsulation in Python
#A class in an example for encapsulation

#Encapsulation is a mechanism where the data (varibles) and the code(methods) thar act on the data eill bind together
class Student:
    #to declear and example for encapsulation
    def __init__(self):
        self.id = 10
        self.name = 'Raju'
    
    #display student details
    def display(self):
        print(self.id)
        print(self.name)
        


#Abstraction 
# The unnecessary data from the user and expose only that data that is of interest to the user. This is called abstraction
# We can write the varible with to double score defore it as: __var. This is like a private varible is Python. In the following example, 'y' is a private varible since it is written as :__y 
'''
class myClass:
    #this is constructor
    def __init__(self):
        self.__y = 3 #this is private varible
        

m = myClass()
print(m.y)

print(m._myClass__y) #display private varible y
'''
#Understanding public and private varibles

class myClassConst:
    #this is constructor.
    def __init__(self):
        self.x = 1 # public var
        self.__y = 2 #private var
        #instance method to access varibles
        def display(self):
            print(self.x) #x is varible directly
            print(self._myClass__y) #name mangling requried

print('Access varibles through method:')
m = myClassConst()
m.display()

print('Accessing varibles through instances:')
print(m.x) #x is available directly
print(m._myClass__y)


#access some part of data 

class Bank:
    def __init__(self):
        self.accno = 10
        self.name = 'Srinu'
        self.balance = 5000.00
        self.__loan = 1500000.00
        
    def display_to_clerk(self):
        print(self.accno)
        print(self.name)
        print(self.balance)


        
        
            
        
