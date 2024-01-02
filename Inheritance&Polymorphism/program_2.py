#A python program to use the teacher class (teacher class define in program_1.py file)
#Import program_1 file for using Teacher class
from program_1 import Teachers

#create instance
t = Teachers()

#Store data into the instance
t.setId(10)
t.setName('Prakash')
t.setSalary(25000)
t.setAddress('Address. xyz, 572406, Ind')

#retrive data from instance and display the value
print('Id : {},\nName: {},\nSalary: {},\nAddress : {}'.format(t.getId(),t.getName(),t.getSalary(),t.getAddress()))


