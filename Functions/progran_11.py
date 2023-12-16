#A python program to know how to pass a function as aparameter to another function
def display(fun):
    return 'Hai '+ fun
def message():
    return 'How are you ?'

x = display(message())
print(x)