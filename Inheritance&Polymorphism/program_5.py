#A Python program to create Student class by deriving it from the teacher class.
#Student class -V2 
from program_1 import Teachers
class Students(Teachers):
    def setMarks(self, marks):
        self.marks = marks
    
    def getMarks(self):
        return self.marks

#Create instance 
s2 = Students()

#Store the value in to the instance

s2.setId(101)
s2.setName('Rakest')
s2.setAddress('HNO-22, XYz, 751850')
s2.setMarks(970)

#Retrive from instance and display the value

print('Id : {}\nName : {}\nAddress : {}\nMarks : {}'.format(s2.getId(),s2.getName(),s2.getAddress(),s2.getMarks())) 