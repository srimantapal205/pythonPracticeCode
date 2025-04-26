#A python program to understand that Myclass method is shared by all of its object
#A class with method

class MyClass:
    def calculate(self, x):
        print('Squre value == ', x*x)

#all object share same calculate() method
obj1 = MyClass()
obj1.calculate(2)

obj2 = MyClass()
obj2.calculate(3)

obj3 = MyClass()
obj3.calculate(4)




