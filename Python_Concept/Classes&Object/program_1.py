#A python program to define Student class an object to it. Also we will call the method and display the student details
#Instance varible and Instance method
class Student:
    #This is a special method call constructor
    def __init__(self):
        self.name = "Vishnu"
        self.age = 15
        self.marks = 900
        
    #this is an instance method.
    def talk(self):
        print('Hi I am {}'.format(self.name))
        print('My age is {}'.format(self.age))
        print('Hi Marks are {}'.format(self.marks))

#create a instance to Student class
s1 = Student()

#Call the method using the instance.

s1.talk()
        