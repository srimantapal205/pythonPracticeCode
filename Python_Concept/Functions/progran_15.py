#A python program to create a new object inside the function doesnot modify outside object
#passing a list to a function
def modify(lst):
    '''To create a new list'''
    lst = [1,2,3,4,5]
    print(lst, id(lst))

#Call modify() and pass lst
lst = [9,8,7,6,5]
modify(lst)

print(lst, id(lst))    
    
    