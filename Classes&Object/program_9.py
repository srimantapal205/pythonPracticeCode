#A python program to create a static method that calculate squre root of given number.
#A static method to find squre root value
import math

class Sample:
    @staticmethod
    def calculate(x):
        result = math.sqrt(x)
        return result

#accept number from user
num = int(input('Enter a number :: '))

#Call the static method and passnum
res = Sample.calculate(num)
print("The square root of {} is {:.2f}".format(num, res))
