#A pthon program to use Student class which is already available in program_3.py file
#Using Students class
from program_3 import Students

#Create instance
s1 = Students()
s1.setId(101)
s1.setName('Rakesh')
s1.setAddress('HNO-22, XYz, 751850')
s1.setMarks(970)

#Display the student details from instance 
print('Id : {}\nName : {}\nAddress: {}\nMarks : {}'.format(s1.getId(),s1.getName(),s1.getAddress(), s1.getMarks()))