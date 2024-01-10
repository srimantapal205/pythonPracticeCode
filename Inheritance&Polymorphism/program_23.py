#A python programing to show method overloading to find sum of two or three number
#method overloading
class MyClass:
    def Sum(self, a=None, b = None, c = None):
        if a != None and b != None and c != None:
            print('Sum of three number :: ', a + b + c)
        elif a != None and b != None:
            print('Sum of two number :: ', a + b)
        else:
            print('Please enter two or three arguments.')

#call Sum using object
m =MyClass()
m.Sum(100,200,300)
m.Sum(400,500)
m.Sum(600)            
        
        