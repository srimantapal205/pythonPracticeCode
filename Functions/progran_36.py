#A python program using lambda function to calculate product of elements of list

from functools import*
lst = [1,2,3,4,5]
result = reduce(lambda x,y: x*y, lst)
print(result)

