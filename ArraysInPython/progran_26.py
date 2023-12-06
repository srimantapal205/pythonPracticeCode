#Using any and all function
from numpy import *

a = array([1,2,3,4,5])
b = array([5,4,3,2,1])

c = a>b

print('Check if any one element is true : ', any(c))
print('Check if all element is true : ', all(c))

if(any(a>b)):
    print("A contains atleast one element greater than those of b")
    
