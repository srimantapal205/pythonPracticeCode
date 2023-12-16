#A python program to know how to define a function inside another function
def display(str):
    def message():
        return 'How are you ?'
    
    result = message() + str
    return result

#Call the function

print(display(" Krishna"))
