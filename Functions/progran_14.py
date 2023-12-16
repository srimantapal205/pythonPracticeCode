#A python program to pass a list to a function and modify it
def modify(lst):
    '''to add a new element to list'''
    lst.append(9)
    print(lst, id(lst))


#call modify() and pass list
list = [1,2,3,4,5,6]
modify(list)

print(list, id(list))