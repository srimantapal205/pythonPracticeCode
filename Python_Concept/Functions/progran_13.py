#A python program to pass an interger to finction and mof=dify it
def modify(x):
    '''Reassigning a value to the varible'''
    x= 15
    print(x, " --of memory address-- :: ", id(x))
#call and modify() and pass x ne  value  
x=10
modify(x)
print(x, id(x))