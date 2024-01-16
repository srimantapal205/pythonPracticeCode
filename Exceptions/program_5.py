#A python program to increment the salary of an employee by 15%
#logical error
def increment(sal):
    sal = sal * 15/100 #this is wron formula so this is a logical error example
    # sal = sal + sal*15/100 this is the coorect formula. 
    return sal

#call the Increment and pass the salary
sal = increment(5000)
print('Incremented salary  == %.2f'%sal)