#A python program to know a function can return anothe function

def display():
    def message():
        return 'How are you ?'

    return message

#Call display() function and it returns message() function in the following code, fun refers to the name function : message

fun = display()
print(fun())



