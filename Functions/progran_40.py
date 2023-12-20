# A python program to apply two decorators to the same function using the @ symbol 
#A decotator that increment the value of a function by 2
def decor_1(fun):
    def inner():
        value = fun()
        return value + 2
    return inner

#A decorator that double the value of a function
def decor_2(fun):
    def inner():
        value = fun()
        return value*2
    return inner

#take a function to which decotar should be applied
@decor_1
@decor_2
def num():
    return 10

#Call the num() function and apply decor_2 the decor_1
print(num())




