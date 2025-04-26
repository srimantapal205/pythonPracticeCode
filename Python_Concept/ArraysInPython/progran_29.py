#Using nonzero() function
from numpy import *
a = array([1,2,0,-1,0,6, 20, 12])

#retive index of non zero element from a
c = nonzero(a)
#display indexes

for i in c:
    print(i)
    
print(a[c])


