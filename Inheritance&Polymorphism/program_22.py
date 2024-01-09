#A python program to overload the multipleaction (*) operator to make itact on object
#Overloading the * operator
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def  __mul__(self, other):
        return self.salary*other.days

class Attendence:
    def __init__(self, name, days):
        self.name = name
        self.days = days

x1 = Employee('Srinu', 500.00)
x2 = Attendence('Srinu', 25)
print('This month salary :: ', x1*x2)        
