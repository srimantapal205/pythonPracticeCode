#A python program to use the assert statement with a message .
#Handling AssertionError - v2
try:
    x = int(input('Enter number between 5 and 10 :: '))
    assert x>5 and x<10, 'Your input is not correct..!'
    print('The number enterd:: ',x)
except AssertionError as obj :
    print(obj)