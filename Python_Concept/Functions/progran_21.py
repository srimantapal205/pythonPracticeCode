#A python program to understand global and local varible
a = 1 #this is global varible
def varFunctionChaeck():
    a = 2 #this is local varible
    print('a == :: ', a, ' This is local Varible')

varFunctionChaeck()

print('a == :: ', a, ' This is Global Varible' )

