#A python program to understand class varible of static varible
class Sample:
    #this is class var
    x = 10

    #this is class methods
    @classmethod
    def modify(cls):
        cls.x += 1

#create 2 instances
s1 =  Sample()
s2 =  Sample()

print('x in s1 == ::', s1.x)
print('x in s2 == ::', s2.x)

#modyfy x in s1
s1.modify()
print('x in s1 == ::', s1.x)
print('x in s2 == ::', s2.x)




    
    