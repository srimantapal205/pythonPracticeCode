#A python program to store data into instance using mutator methods and to retrive data from the instance using accessor methods
#Accessor and mutator methods

class Students :
    
    #mutator methods
    def setName(self, name):
        self.name = name
    
    #accessor method
    def getName(self):
        return self.name
    
    #mutator method
    def setMarks(self, marks):
        self.marks = marks
    
    #accessor methods
    def getMarks(self):
        return self.marks
    
#Create instance with some data from keyboard
n = int(input('How many students? :: '))
    
i =0

while(i<n):
    #create student class instance
     s = Students()
     name = input('Enter name :: ')
     s.setName(name)
     
     marks = int(input('Enter marks :: '))
     s.setMarks(marks)
     
     #retrive data from student class instance
     print('Hi ', s.getName())
     print('Your marks :: ', s.getMarks())
     i += 1
     print('--------------------------------------------')



     
        
    
    