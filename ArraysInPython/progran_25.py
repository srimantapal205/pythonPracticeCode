 #A python program tp compare two array
from numpy import *

a = array([1,2,3,4,5])
b = array([5,4,3,2,1])

c = a==b
print("Result of a== b :: ", c)

c = a>=b
print("Result of a=>b :: ", c)
 
c = a<=b
print("Result of a<=b :: ", c)

