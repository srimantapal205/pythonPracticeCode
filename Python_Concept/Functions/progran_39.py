#A python program to create two decorator function

#A decorator function that increament the value of a function by 10
def decor(fun):
    def inner():
        value = fun()
        return value+10
    return inner

#A decorator function that double the value of a function

def decor2(fun):
    def inner():
        value = fun()
        return value*2
    return inner

#Take a function to which decoratoor should be applied
def num():
    return 10

#callnum() function and apply decor1 and then decor 
result_fun = decor(decor2(num))

print(result_fun())




