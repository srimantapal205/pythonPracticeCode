#Write a program to understand how a function return multiple value
def sum_sub(a, b):
    '''This function return result of addition and subtraction of a & b'''
    c = a+b
    d = a-b
    return c, d

#get the result from sum_sub() functio 
x, y = sum_sub(30, 20)
print('The result of addition :: ', x)
print('The result of subtraction :: ', y)
    
    