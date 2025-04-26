#A python program using a student class with instance methods to process the data of several students
#instance methods to process data of the object
class Students:
    #this is constructor
    def __init__(self, n='', m = 0):
        self.name = n
        self.marke = m
    
    #this is an instance method
    def display(self):
        print('Hi ', self.name)
        print('Your markss ', self.marke)
        
    #to calculate grade based on marke
    def calculate(self):
        if(self.marke >= 600):
            print('You got First Grade')
        elif(self.marke >= 500):
            print('You got Second Grade')
        elif(self.marke>400):
            print('You got Third Grade')
        else:
            print('You are faild')

#Create instance with some data  from keyboard
n = int(input('How many students ? '))

i = 0

while(i<n):
    name = input('Enter Student Name :: ')
    marks = int(input('Enter Marks :: '))
    
    #Create student class instance and store data
    s = Students(name, marks)
    s.display()
    s.calculate()
    i+=1
    print('........................................................................................................')

        
        
        