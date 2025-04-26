#using where() function
from numpy import *
a = array([10,20,30,40,50,60], int)
b = array([1,21,3,40,50,51], int)

#if a>b then take element from a else b

c = where(a>b, a, b)
print(c)

