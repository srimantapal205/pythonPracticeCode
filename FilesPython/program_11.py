#A python program to create an Emp class with employee details as instance varible.
#Emp class 
class Emp:
    def __init__(self, id, name, sal):
        self.id = int(id)  # Convert id to integer
        self.name = name
        self.sal = float(sal)  # Convert sal to float
        
    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id, self.name, self.sal))
        