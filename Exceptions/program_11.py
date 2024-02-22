#A python program to understand the usage of try with finally blocks
try:
    x = int(input('Enter a number :: '))
    y = 1 / x
finally:
    print("We are not catching the exception.")
print('The invers is :: ', y)
