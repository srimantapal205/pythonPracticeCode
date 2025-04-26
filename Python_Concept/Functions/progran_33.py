#A python program to find squares of elements in a list
#map() function that gives squares 

def squares(x):
    return x*x

#list of numbers
lst = [1,2,3,4,5,6,7,8,9]

#call map() with squares()
newLst = list(map(squares, lst))
print(newLst) 
