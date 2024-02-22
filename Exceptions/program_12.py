#A python program to assert statement and catching AsssertionError 
#Handling AssertionError
try:
    x = int(input('Enter Number Between 5 and 10 :: '))
    assert x>5 and x<10
    print('The Number enterd :: ',x)
except AssertionError:
    print('The condition is not fullfilled')
