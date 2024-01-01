#Apython program to claculate power value of a member with the help of a static method
class MyClass:
    #method to calculate X to the power of n
    @staticmethod
    def mymethod(x,  n):
        result = x**n
        # return result
        print('{} to the power of {} is {}'.format(x, n, result))
#Call the static method
MyClass.mymethod(5, 3)
MyClass.mymethod(5, 4)
