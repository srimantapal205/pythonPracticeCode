#To handle assertion Error raised by assert
x = int(input('Enter a number greater than 0: '))
try:
    assert(x>0) #exception may occure there
    print('You enterd: ', x)
except AssertionError:
    print('Wrong input enterd') #this is exeute in case of exception