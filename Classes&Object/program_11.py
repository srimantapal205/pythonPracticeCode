#Apython program to create emp class and make all the member of the EMP class available to another class
#Passing members of one class to another class
class Emp:
    #this is constractor
    def __init__(self, id, empName, salary):
        self.id = id
        self.empName = empName
        self.salary = salary
    
    #this is an instance method
    def display(self):
        print('Id = ', self.id)
        print('Emp Name = ', self.empName)
        print('Salary = ', self.salary)
        

class MyClass:
    #method to recive Emp class instance and display employee details
    @staticmethod
    def myMethod(e):
        #increment salaray for 1000
        e.salary += 1000
        e.display()
        

#create emp class instance e
e = Emp(10, 'Raj Kumar', 15000.75)
#Call static methods of MyClass and pass e
MyClass.myMethod(e) 
