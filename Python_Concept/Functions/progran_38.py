#A python program to apply a decorator to a function using @ symbol
#A decorator that increment the value of a function by 2
def decor(fun): #this is decorator function
    def inner(): #this is the inner finctionthat modifies 
        value = fun()
        return value+10
    return inner # return inner function

#take a function which decorator should be applied
@decor #apply decor to the below function
def num():
    return 10

#call num() function and display it's result
print(num())



