#Namespace

#Understand class name space
class Student:
    #this is class var
    n=10
    
#access class var in the class name space
print(Student.n) #Display 10

Student.n += 1 #Modify it in class namespace
print(Student.n) #Display 11 


#---------------------------------------------------

#Understanding the instance name space
class StuInstance:
    #this is class varible
    n = 10
#Access class var in the s1 instance name space
s1 = StuInstance()
print(s1.n) #Display 10
s1.n += 1
print(s1.n)

#modified class varible is not seen in other instance
s2 = StuInstance()
print(s2.n)
s2.n +=2
print(s2.n)
