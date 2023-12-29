#A pthon program to understand instance varible
#instance vars example

class Sample:
    #this is constractors.
    def  __init__(self):
        self.x = 10
    
    #This is istance method
    def modify(self):
        self.x+=1
    
#Create 2 instances
s1 = Sample()
s2 = Sample()

print('x in S1 == :: ', s1.x)
print('x in S2 == :: ', s2.x)

#modify x in s1
s1.modify()
print('x in S1 == :: ', s1.x)
print('x in S2 == :: ', s2.x)






    