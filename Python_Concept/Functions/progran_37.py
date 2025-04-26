#A decorate to increase the value of a function
#A decetor that increament the value of function by 2

def decor(fun): #This is decetor function 
    def inner():#this is inner function that modifies
        value = fun()
        return value +2
    return inner
#take a function to which decetor should be applied
def num():
    return 10

#Call the decetor function and pass num
result = decor(num) # Result represent inner function 
print(result()) #Call result and display the result