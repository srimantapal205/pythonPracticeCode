#Using logical_and(), logiacl_or(), logical_not() 

from numpy import *

a = array([1,2,3], int)
b = array([0,2,3], int)

c = logical_and(a>0, a<4)
print(c)

c = logical_or(b>0, b==1)
print(c)

c = logical_not(b)
print(c)
